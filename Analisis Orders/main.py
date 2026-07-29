import  webbrowser as wb

def open_youtube(name):
    # Use a breakpoint in the code line below to debug your script.
    youtube = wb.open_new_tab('https://www.youtube.com/@imMohammedMustafa/search?query=' + name)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_youtube('python')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
