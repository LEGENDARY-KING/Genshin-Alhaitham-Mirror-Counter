# Genshin Alhaitham Mirror Counter

This is a Python project that counts the number of mirrors in the game Genshin Impact using keyboard and mouse input monitoring.

## Getting Started - Release version

1. Download the latest release from GitHub.
2. Check the config.ini file and edit it accordingly
3. Run the program as an administrator. This is necessary as Genshin Impact must be run as an administrator and the program needs administrative privileges to monitor keyboard and mouse inputs.

## Getting Started - Manual version
1. Download the source code by either cloning the repository using git or by downloading the source code as a zip file.
    - To clone the repository, run the command `git clone https://github.com/LEGENDARY-KING/Genshin-Alhaitham-Counter.git`
    - To download the source code as a zip file, go to the GitHub page and click on "Clone or Download" and then "Download Zip"
2. Ensure that you have Python and pip installed and updated.
3. Run `pip install -r requirements.txt` to install all the required packages.
4. Check the config.ini file and edit it accordingly
5. Run the file `main.py` as an administrator. This is necessary as Genshin Impact must be run as an administrator and the program needs administrative privileges to monitor keyboard and mouse inputs. 
    - To run the `main.py` file, navigate to the project directory in the command line as administrator and run `python main.py`
6. Use the `setup.py` file to create an executable file for yourself, if desired.
    - To run the `setup.py` file, navigate to the project directory in the command line and run `python setup.py build` and then it will generate a build folder where you will be able to find an exe file that you need to also run as administrator


If you want to use this over the genshin impact window then download 

## Additional Information
- This tool does not use image recognition, so the results may not be 100% accurate and may include mirrors generated when the character does not have enough energy, or when charged or plunge attacks do not actually hit any enemies.
- Known Bugs:
    1. If pressing the window of the exe after directly coming from game the system freezes for a bit, just click the button again and for future press on anything else before pressing the window navigation portion
    2. Plunge attack based mirrors do not count accurately

**Disclaimer:** We are not responsible for any account bans or suspensions that may occur while using this program. While this program does not interact directly with the game, it is important to use it responsibly and at your own risk.

If you have any issues or suggestions, please open an issue on the GitHub page.

## Contributing

If you are interested in contributing to this project, please open a pull request on the GitHub page.

## Author

* **LEGENDARY KING**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
