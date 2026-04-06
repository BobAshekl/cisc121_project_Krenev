
import gradio as gr
#Panda is used for Creating DataFrame's
import pandas as pd
import random
#Ploty is used to make gradio plots dynamic as earlier editions struggling to visualize changes in the data frame
import plotly.express as px

def arr_builder(): #This function creates a list of random size and with random values
    arr = []

    for x in range(random.randint(5, 10)):
        arr.append(random.randint(1, 10))

    #This puts the list into a dataframe with colors as an extra dimension
    df = pd.DataFrame({
        "position": range(len(arr)),
        'value': arr,
        "color": ["normal"] * len(arr)
    })

    
      
    return make_plot(df), df, df.copy(), 0, False, gr.Timer(active=False), "New Array has been built"
def make_plot(df): #Creates visual plot of dataframe df
    vis = px.bar( 
        df,
        x="position",
        y="value",
        color="color",
        color_discrete_map={
            "normal": "#4C72B0",   #base color (blue)
            "red": "#F33B03",  # selected index's for comparison (red)
            "sorted": "#00FF40" # Color of sorted array (green)

        }
    )
    #updates on the default plot to make it more visually apealling. barmode = overlay is needed for dynamic movements in the plot when swaps are made
    vis.update_layout(barmode = "overlay", template = "plotly_dark", showlegend = False,margin=dict(l=40, r=40, t=20, b=40), xaxis_title=None,yaxis_title=None)
    vis.update_traces(width = 0.8, texttemplate="%{y}", textposition="outside")
    vis.update_xaxes(showticklabels=False, showgrid=False)
    vis.update_yaxes(showticklabels=False)

    return vis
    
def swap(df, index, swapped): #swap is goes through one step in the sorting algorithim
    #Creates copy for reset()
    df = df.copy()
    df["color"] = "normal"
    n = len(df)
    
    if index >= n-1: #Checks if index is larger or equal to data frame length
        if not swapped: #Checks if swap occured last itteration if not then array is sorted and bars change color to green
            df["color"] = "sorted"
            index = 0
            swapped = False 
            return make_plot(df), df, index, swapped, "Array is sorted"
        #If swapped = True then array is not sorted and index resets to zero
        index = 0
        swapped = False 
        return make_plot(df), df, index, swapped, "Pass through complete, Starting again" 
    #variables a and b are used to make explanation more readable
    a = df.loc[index, "value"]
    b = df.loc[index + 1, "value"]
    df.loc[index,"color"] = "red"
    df.loc[index+1,"color"] = "red"
    #Checks if swap needs to occur and swaps values at indexes
    if df.loc[index,"value"] > df.loc[index+1,"value"]:
        df.loc[index,"value"], df.loc[index+1,"value"] = df.loc[index+1,"value"], df.loc[index,"value"]
        swapped = True
        explanation = f"{a} and {b} have swapped places as {a} > {b}"
    else:
        explanation = f"No swap occurs as {a} is equal or smaller than {b}"
    index +=1
    
    
    return make_plot(df), df, index, swapped, explanation
    
def timer_starter():# timer_starter() and timer_stopper() are used to change the state of the timer
    return gr.Timer(active=True)
def timer_stopper():
    return gr.Timer(active=False)
    
def play(df, index, swapped):
    #Creates copy for reset()
    df = df.copy()
    df["color"] = "normal"
    n = len(df)

    
    if index >= n-1:#Checks if index is larger or equal to data frame length
        if not swapped:#Checks if swap occured last itteration if not then array is sorted and bars change color to green
            df["color"] = "sorted"
            index = 0
            swapped = False 
            explanation = "Array has been sorted"
            
            return make_plot(df), df, index, swapped, gr.Timer(active=False), explanation
        #If swapped = True then array is not sorted and index resets to zero
        explanation = "pass through complete, starting at beginning"
        index = 0
        swapped = False 
        return make_plot(df), df, index, swapped, gr.Timer(), explanation

    #variables a and b are used to make explanation more readable
    a = df.loc[index, "value"]
    b = df.loc[index + 1, "value"]

    df.loc[index,"color"] = "red"
    df.loc[index+1,"color"] = "red"
    #Checks if swap needs to occur and swaps values at indexes
    if a > b:
        df.loc[index,"value"], df.loc[index+1,"value"] = df.loc[index+1,"value"], df.loc[index,"value"]
        swapped = True
        explanation = f"{a} and {b} have swapped places as {a} > {b}"
    else:
        explanation = f"No swap occurs as {a} is equal or smaller than {b}"
    index +=1

    
    return make_plot(df), df, index, swapped, gr.Timer(), explanation
def reset(original_df): #function recalls original state of data frame to set plot back to original state
    
    df = original_df.copy()
    df["color"] = "normal"
    
    return make_plot(df), df, 0, False, gr.Timer(active=False), "Array has reset"
def speed_update(new_speed): #Uses slider value to change speed of timer
    return gr.update(value = new_speed)


with gr.Blocks() as demo:
    #Gradio uses State value instead of variables
    state_df = gr.State()
    state_index = gr.State(0)
    state_swapped = gr.State(False)
    state_original_df = gr.State() 
    
    gr.Markdown("Bubble Sort Visualizer")
    
    timer = gr.Timer(0.5, active= False) #Timer defaults to 0.5 speed and being off to ensure the play function does not start before the user presses it

    with gr.Row(): #gr.Row() puts all objects inside of it on the same row for apperance

        
        with gr.Column(scale=3): #gr.Column() puts the plot and the explantion on the same collumn so the explanation is under the plot. scale = 3 is set so the array has enough space
            
            bar = gr.Plot()
            explanation = gr.Markdown("Ready")

        
        with gr.Column(scale=1): #This puts the button on the next collumn to the right of the plot for apperance
            btn_random = gr.Button("Randomize")
            btn_play = gr.Button("▶ Play", variant="primary") # symbols found in windows emoji libary (win + .) for visual apeal
            btn_step = gr.Button("⇨ Step")
            btn_stop = gr.Button("□ Pause")
            speed = gr.Slider(0.1, 1.5,value=0.5,step=0.1,label="Speed")
            btn_reset = gr.Button("↺ Reset")
    #This checks if the timer active = True and runs the play() function       
    timer.tick(fn = play, inputs = [state_df,state_index, state_swapped], outputs = [bar,state_df,state_index,state_swapped, timer, explanation])
    

    #updates the speed if slider value changes
    speed.change(fn = speed_update, inputs = speed, outputs= timer)
    #runs arr_builder()
    btn_random.click(fn = arr_builder, inputs = None, outputs = [bar,state_df,state_original_df, state_index, state_swapped,timer, explanation])
    #runs swap()
    btn_step.click(fn = swap, inputs= [state_df,state_index, state_swapped], outputs = [bar,state_df,state_index,state_swapped, explanation])
    #runs timer_starter()
    btn_play.click(timer_starter,None, timer)
    #runs timer_stopper()
    btn_stop.click(timer_stopper,None, timer)
    #runs reset()
    btn_reset.click(fn = reset, inputs = state_original_df, outputs = [bar, state_df, state_index, state_swapped, timer, explanation])
#launches gradio with blocks
demo.launch()