

# cisc121_project_Krenev


https://github.com/user-attachments/assets/38daf59d-128c-4961-92ee-b994f61ea4ca

https://github.com/BobAshekl/cisc121_project_Krenev/blob/6d0eea0cc7af17c8504cad9bd6a727cecfa7f07a/Krenev_DemoVideo.mp4
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
# Testing
As most of the user input comes from the form of clicking a button There were not many edge cases to test
When buttons were repeatly pressed Function worked as normal
The only edge case that I could test was the slider with inputs outside of its range which results with: 

<img width="814" height="547" alt="image" src="https://github.com/user-attachments/assets/2d9038e0-8b0d-48e9-9eec-a2c8da6117d9" />

Though when actually run the program just runs with the closest number possible to the inputed value

<img width="530" height="441" alt="image" src="https://github.com/user-attachments/assets/80e07cd2-dbb1-41c3-9184-16b586d84b22" />

This result is the same when testing an input smaller than 0.1 and if the input is not a number the slider just doesnt accept it and defaults to 0.5

# Running the program
```
pip install gradio
```
or 
```
python -m pip install gradio
```
Then run 
```
python app.py
```
Or using the app launched on hugging app with: https://huggingface.co/spaces/bobashekl/cisc121_project_Krenev

# Acknowledgment
Author: Daniel Krenev or Bob Ashekl
Purpose: final project for CISC 121 at Queen's University
Disclaimer: Copilot was used throughout the development of this application to explain functions in gradio as documentation for gradio was often lacking for implementation of Button() and Timer() function. Code was written by Daniel Krenev

