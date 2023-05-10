# Young Tableaux Generator
This program generates all Young tableaux with the specified height and number of remaining columns, 
and displays them in a GUI using tkinter. 
A Young tableau is a way of representing a partition of a positive integer by arranging its parts
in a two-dimensional array so that the parts are weakly increasing along each row and strictly increasing down each column.

### Dependencies:
- Python 3.x
- tkinter
~~- Pillow~~
Installation
1. Download and install Python 3.x from the official website: https://www.python.org/downloads/
2. Install tkinter by running one of the following commands**:
3. a) On Windows: pip install tkinter
   b) On macOS: sudo pip3 install tkinter
     ** if python is already installed(specially on macOS) a common error is 
     "import _tkinter # If this fails your Python may not be configured for Tk
     ImportError: No module named _tkinter"
     - To fix this, install python with the package specification: brew install python-tk
   
### Usage:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the young_tableaux.py file.
3. Type the following command and press Enter: python3 young_tableaux.py
4. Enter the desired values for n and m in the input fields(m & n > 0). 
5. Click the 'Generate' button.
6. The program will generate and display all valid Young tableaux in the output box, 
   along with a count of the total number of tableaux generated(|λ|).
   
   ***Executble file not currently working due to github's size compatibility but available upon request***
   
### Contributing:

**Contributions to this project are welcome! To contribute:**

1. Fork this repository.
2. Create a new branch with your changes: git checkout -b my-feature-branch
3. Make your changes and commit them: git commit -m "Added my feature"
4. Push your changes to your fork: git push origin my-feature-branch
5. Create a pull request from your fork to the original repository.


### Contact:
Name: Rafael L.S Reis
Email: rafael.ls.reis@gmail.com

### License:
This program is licensed under the MIT License. See the LICENSE file for more information.
