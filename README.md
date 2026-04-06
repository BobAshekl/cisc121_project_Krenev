

# cisc121_project_Krenev

# Bubble Sort
  I chose to develop my visualizer app with bubble sort as the focus because of its significance as a stepping stone when learning sorting algorithms and how to implement them in your projects

# Bubble Sort Step by Step

  - Bubble sort starts by comparing the first two elements at index's zero and one. 
    - If the element at index zero is larger than the element at one: The elements swap indexes.    
    - If the element at index one is larger than no swap occurs.    
  - Bubble sort than repeats this comparison with the second element in the previous comparison with the next one after it.
  - Once Bubble sort has gone through all index's in the array it repeats the previous logic until the list is solved.
# Abstraction

  This code is designed to have a simple linear process to make it as easy as possible for users new to this algorithms can follow along through both the app and the code that makes it work. 
  
  This code uses gradio which could lead to confusion for people like me (before working on this project) who are not experienced with gradio. For this reason, The logic behind the bubble sort has mostly been isolated in the play() and step() functions 
  
  in the form:


  
    if a > b:
  
        df.loc[index,"value"], df.loc[index+1,"value"] = df.loc[index+1,"value"], df.loc[index,"value"]
        
        swapped = True
        
        explanation = f"{a} and {b} have swapped places as {a} > {b}"
        
    else:
    
        explanation = f"No swap occurs as {a} is equal or smaller than {b}"
        
    index +=1
    
  To futher assit the user in understanding this algorithim explanations to why a swap/no swap occured with a text box giving the explanation right under the visual list.

# Design
  This program lets the user generate a random array that can be interacted with either the play button which starts a timer that goes through steps at a regular interval leading to the output of the sorted list or a step button that causes the program to go through one step in the algorithim leading to the output of one step closer to a sorted list. 
  
  The play function also comes with a slider to adjust speed and a pause button that stops the timer until play is pressed again. 
  
  The last button in this program is the reset button which returns the array back to how it started.

  The design of the program is delibiratley made to make user inputs as simple as possible to avoid problems with unknown inputs
