import getpass
import psutil
import wmi
import difflib
import subprocess
import random
import string
import cmd
import os
import sys
import datetime
import shutil


class ShellStats:
      
      name = "PyConsole"
      Version = "0.0.5"
      Producer = "PythonCMD Inc." # Disclamer, this is not a real company.
      Copyrighted = False
      CopyrightText = "" # Will Change if Copyrighted Is True.  

class PyConsole(cmd.Cmd):

    intro = 'Welcome to PyShell Type help or ? to list commands.\n'
    prompt = 'PyConsole '

    global Launch_Security
    Launch_Security = True


    def do_amountCMD(self, arg):
        """Says how many commands there are.
        """

        COMMANDS = ["amountCMD","TASKLIST","settings","launch","show_os_name","whoami","show_computer_stats","remove_from_path","add_to_path",
              "file_differences","grep","chmod","kill","edit","move_file","copy_file","copy_data","file_stats","time","env",
              "create_file","cd","echo","rename_file","quit","ls_format","clear","ls","read","mkdir","rmfil","rmdir","credits"]

        print(len(COMMANDS))

    def do_downloadversion(self, arg):
        if arg == "0.0.3":
            print("This feature is new.")
            raise AttributeError("No such attribute named 'downloadversion'. Check the documents found in the README.md")
            
        
    def do_TASKLIST(self, arg):
        """Shows every working task.

        Usage: TASKLIST

        """

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username','cpu_percent','status'])
            except psutil.NoSuchProcess:
                 pass

            else:
                # Print process details
                print(pinfo)

    def do_settings(self, arg):
        """Changes a setting of a command.

        Usage: settings [setting]

        example: settings launch safety

        output: Do you want to turn launch safety off? Yes
                (Turns off the launch security.)

        """
        
        Available_Settings = ["Launch Safety"]

        global Launch_Security

        if arg.lower() == "launch safety":
            Launch_Safety = input("Do you want to turn launch safety off? ")
            
            if Launch_Safety.lower() == "yes":
                Launch_Security = False

        elif arg.lower() == "list settings":
            for i in Available_Settings:
                print(i)
        
    def do_launch(self, arg):
        """Launches the specified app.

        Usage: launch [application_name]

        example: launch notepad.exe

        output: (it launches notepad/notepad.exe)

        """

        try:
            if (arg == "google.exe" or arg == "chrome.exe" or arg == "chrome" or arg == "google"):
                subprocess.run("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")

            elif (arg == "notepad" or arg == "notepad.exe"):
                subprocess.run("notepad.exe")

            elif (arg == "youtube" or arg == "youtube.exe" or arg == "yt"):
                
                subprocess.run("""C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe  --profile-directory="Profile 4" --app-id=agimnkijcaahngcdmfeangaknmldooml""")

            elif (arg == "roblox.exe" or arg == "roblox" or arg == "rbx"):

                subprocess.run("""C:/Users/User/AppData/Local/Roblox/Versions/version-dc61c2db7d694b7b/RobloxPlayerLauncher.exe -app""")

            elif (arg == "Devforum.exe" or arg == "Devforum" or arg == "DevInfo"):
                subprocess.run(""""C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe"  --profile-directory="Profile 4" --app-id=gcboekedeadipgppalmbgpgeojfpbgef""")

            elif (arg == "Vscode" or arg == "vscode" or arg == "vscode.exe" or arg == "visual studio code"):
                
                subprocess.run("C:/Users/User/AppData/Local/Programs/Microsoft VS Code/Code.exe")

            else:
                if Launch_Security:
                    SecurityInput = input("This application might execute malicious code, If you want to continue say yes. ")
                    
                    if SecurityInput.lower() == "yes":
                        subprocess.run(arg)

                    else:
                        return False
                    
                else:
                    subprocess.run(arg)

        except FileNotFoundError:
            print("Cannot launch application since it might not exist or you entered the wrong application name.")

    def do_show_os_name(self, arg):
        """Echoes the os name.

        Usage: show_os_name

        """

        self.do_echo(os.name)

    def do_whoami(self, arg):
        """Echoes the user's name.

        Usage: whoami

        """
        user = getpass.getuser()
        print(f"You are: {user}")

    def do_show_computer_stats(self, arg):
        """Prints the computer's status.

        Usage: show_spec

        """
        # Connect to WMI service
        wmiService = wmi.WMI()
        
        # Get CPU information
        cpu = psutil.cpu_freq()

        # Print CPU information
        print("CPU Frequency:", cpu.current, "MHz")
        print("CPU Usage:", psutil.cpu_percent(), "%")

        # Get hard drive information
        for physical_disk in wmiService.Win32_DiskDrive():
            print("Hard Drive Model:", physical_disk.Model)
            print("Hard Drive Capacity:", int(physical_disk.Size) / 1024 / 1024 / 1024, "GB")
            
        # Get memory information
        for mem_module in wmiService.Win32_PhysicalMemory():
            print("Memory Type:", mem_module.MemoryType)
            print("Memory Capacity:", int(mem_module.Capacity) / 1024 / 1024, "MB")

    def do_remove_from_path(self, arg):
        """Removes the selected path

        Usage: remove_from_path [directory]

        example: remove_from_path test

        output: env
                ['wowies']
        
        """

        if os.path.isdir(arg):
            sys.path.remove(arg)
        else:
            print("It might be a file or it does not exist")

    def do_add_to_path(self, arg):
        """Adds the selected path

        Usage: add_to_path [directory]

        example: add_to_path test

        output: env
                ['wowies','test']
        
        """

        if os.path.isdir(arg):
            sys.path.append(arg)
        else:
            print("It might be a file or it does not exist")
    

    def do_file_differences(self, arg):
        """Echoes the differences between 2 files.
         
        Usage: file_differences [file_name]

        example: file_differences Main.py

        output: Put the other file's name: Test.py
                -import this
                -
                -Y = true

                +X = True
        """
        arg1 = input("Put the other file's name: ")
        with open(arg,"r") as f1, open(arg1,"r") as f2:
            f1_contents = f1.readlines()
            f2_contents = f2.readlines()

            diff = difflib.unified_diff(f1_contents,f2_contents)
            print("\n".join(diff))

    def do_grep(self, arg):
        """Echoes out the selected words in that file.

        Usage: grep [file_name]

        example: grep test.py

        output: What do you want the word to be found? import
                import this
                import subprocess

        """

        try:
            To_Look = input("What do you want the word to be found? ")
            
            
            if len(To_Look) == 0:
                print("Needs a word.")
                
            elif To_Look.isspace():
                print("Requires a word not blank.")

            else:   
                command = f"findstr {To_Look} {arg}"
                results = subprocess.check_output(command,shell=True).decode()
                print(results)
        except:
            pass

    def do_chmod(self, arg):
        """Changes the permission of the selected file

        Usage: chmod [file_name]

        example: chmod test.py

        output: 
        """

        mode = int("124755", 8)

        os.chmod(arg,mode)

    def do_kill(self, arg):
        """Quits the terminal.

        Usage: kill

        """
        return True

    def do_edit(self, arg):
        """Edits the contents of the selected file.

        Usage: edit [file_name]

        example: edit test.py

        output: print("Hello world")
        
        edited version: H = 10
                        print(H)

        """

        with open(arg) as f:
            subprocess.Popen(["notepad.exe", arg])

    def do_move_file(self, arg=None,arg1=None):
        """Moves the selected file

        Usage: move_file [file_name]

        example: move_file test.py

        output: test.py has been moved to C:/Users/User/Documents

        """

        if arg is None:
            print("Missing Arg!")

        elif arg1 is None:
            New_path = input("Where to place the file? ")
            New_path = New_path.replace("\\","/")
            shutil.move(arg,New_path)
            print(f"{arg} has been moved to {New_path}")

    def do_copy_file(self, arg, arg1=None):
        """Copies the file."""
        
        if arg1 == None:
            arg1 = input("Name of the file: ")

        try:
            shutil.copy(arg, arg1)
            print(f"File {arg} has been copied into {arg1}")
        except FileNotFoundError:
            print(f"{arg} has not been found, it might be a typo or this file doesn't exist.")
        except PermissionError:
            print("Permissions protected this file, I recommend copying the source to another file.")

    def do_copy_data(self, arg=None, arg1=None):
        """Copies the lines of the file from one location to another."""
        if (arg is None or arg1 is None):
            arg = input("Enter source file: ")
            arg1 = input("Enter destination file: ")
        
        try:
            shutil.copy2(arg, arg1)
            print(f"File '{arg}' copied to '{arg1}'")
        except FileNotFoundError:
            print(f"{arg} has not been found, it might be a typo or this file doesn't exist.")
        except PermissionError:
            print("Permissions protected this file, I recommend copying the source to another file.")

    def do_file_stats(self,arg=None):
        """Gives the stats/status of the file.

        Usage: file_stats [file name]

        example: Test.py
        
        Test.py

        3.99 kb

        """

        if arg is None: 
            print("Needed argument")
        
        try:
          path = arg

          stats = os.stat(path)

          file_size = stats.st_size
          file_name = os.path.basename(path)
           
          print(f"File name: {file_name}")

          if file_size > 999 and file_size < 999999:
              file_size_kb = file_size / 1024
              print("File size: {:.2f} KB".format(file_size_kb))
          elif file_size > 999999 and file_size < 999999999:
              file_size_mb = file_size / (1024 * 1024)
              print("File size: {:.2f} MB".format(file_size_mb))
          elif file_size > 999999999:
              file_size_gb = file_size / (1024 * 1024 * 1024)
              print("File size: {:.2f} GB".format(file_size_gb))
          else:
              print("File size: {} bytes".format(file_size))


        except OSError as e:
            print(e)

    def do_time(self, arg):
        """Echo's the current time. 

        Usage: time

        example: time

        output: 2023-04-18 10:31:15

        """
        print(datetime.datetime.now())

    def do_env(self, arg):
        """Shows the path enviroment.

        Usage: env

        """
        print(f"Sys: {sys.path}")

    def do_create_file(self, arg):
        """Creates a new file.

        Usage: create_file [File_Name]

        example: create_file Hi.py

        output: Hi.py has been created.
                Do you want to write to this file? Yes
                Type in what you want to write: print("Hello World")

        """

        try:
          with open(arg,"w") as f:
            print(f"{arg} has been created.")

            Option = input("Do you want to write to this file? ")

            if Option.lower() == "yes":
                Write = input("Type in what you want to write: ")
                f.write(Write)


            elif Option.lower() == "y":
                Write = input("Type in what you want to write: ")
                f.write(Write)
        except FileExistsError:
            print(f"{arg} exists already. Try creating another file.")



    def do_cd(self, arg):
        """Change the current working directory to the given directory.

        Usage: cd [directory]

        If no argument is given, change to the user's home directory.
        If the argument is '/', change to the root directory.
        """
        if arg == '':
            os.chdir(os.path.expanduser("~"))
            print(f"Changed directory to '{os.getcwd()}'")
            os.environ['PWD'] = os.getcwd()
        elif arg == '/':
            # If argument is '/', change to the root directory of the current drive
            os.chdir('/')
            print(f"Changed directory to '{os.getcwd()}'")
            
            os.environ['PWD'] = os.getcwd()
        else:
            try:
                os.chdir(arg)
                print(f"Changed directory to '{os.getcwd()}'")
                os.environ['PWD'] = os.getcwd()
            except FileNotFoundError:
                print(f"Directory '{arg}' does not exist")
            except NotADirectoryError:
                print(f"'{arg}' is not a directory")

    def do_echo(self, arg):
        """Says the argument provided
        Usage : echo [Message]

        Example: echo Hi
        """
        print(arg)

    def do_rename(self, arg=None):
        """Renames the selected file.
        """

        if arg is None:
            print("You have not inputted arg yet!")
        else:
            New_Name = input("Put the new name: ")
            os.rename(arg,New_Name)

    def do_quit(self, arg):
        """Quits the command prompt.

        Usage: quit

        This command quits the command prompt as soon as you enter the command.
        """
        return True

    def do_ls_format(self,arg):
        """Specifies the listed files to a letter inputted

        Usage: ls_format [Word]

        example: ls_format u

        output: utilities.py
                chat.utils.py

        """
        if arg:
           if len(arg) == 1:
            word = arg.upper()
            filtered_files = [f for f in os.listdir('.') if word in f.upper()]
            for f in filtered_files:
              print(f)
           elif len(arg) > 1:
               print("That is a word.")
        else:
          print("Missing argument. Usage: ls_format [word]")

    def do_clear(self, arg):
        """Clears the terminal screen.

        Usage: clear

        """

        if ShellStats.Copyrighted:
            if os.name == "posix":
                os.system('clear')
            elif os.name == 'nt':
                os.system('cls')
            print(ShellStats.CopyrightText)
        else:
            if os.name == "posix":
                os.system('clear')
            elif os.name == 'nt':
                os.system('cls')

    def do_ls(self, arg):
        """List the files and directories in the current directory.

        Usage: ls

        This command lists the names of all the files and directories in the
        current working directory.
        """
        files = os.listdir('.')
        for f in files:
         print(f)

    def do_read(self, arg):
        """Read's the contents of the file
        
        Usage: read [file]

        example: read Hi.txt

        output: Hi

        """

        if arg:
            with open(arg,"r") as f:
             lines = f.readlines()

             for line in lines:
                 print(line)
        else:
            print("Required File Name.")

    def do_mkdir(self, arg):
        """Makes Directories

        Usage: mkdir[Directory Name]

        This command makes a new Directory in the path you are currently
        in.

        """
        try:
            os.makedirs(arg)
            print(f"Created directory Named '{arg}'")
        except FileExistsError:
            print(f"Directory '{arg}' already exists")

    def do_rmfil(self,arg):
        """Removes the specified file
        
        Usage: rmfil [file]

        example: rmfil test.py

        output: file has been removed.

        Note: Be cautious of using this command.

        """
        try:
            os.remove(arg)
            print(f"Removed {arg}")
        except:
            print("There is an error.")

    def do_rmdir(self,arg):
        """Removes Directories

        Usage: rmdir[Directory Name]

        This command removes a Directory in the path you are currently
        in.

        """
        try:
            os.rmdir(arg)
            print(f"Deleted The Directory {arg}")
        except FileNotFoundError:
            print(f"File Does Not Exist Or Has Been Deleted")

    def do_credits(self,arg):
        """Gives the credits to the creators.

        Usage: credits

        """
        
        self.do_echo("Created by oinky0212 the youtuber, with the help of chatGPT.")

    def precmd(self, line):
        if line.strip() == "--version":
            print("Version is 0.0.3")
            return ""
        elif line.strip() == "ls --format":
            arg = input("Pick your letter: ")
            self.do_ls_format(arg)
            return ""
        elif line.strip() == "!!":
            Whole_Word = ""
            for i in range(10):
               Word = random.choice(string.ascii_lowercase)
               Whole_Word = Whole_Word.join(Word)
               print(Whole_Word,end="")
            return ""
        elif line.strip() == "/":
            self.do_help(arg="")
            return ""
        else:
            return line
        

def run():
    if __name__ == '__main__':
        if ShellStats.Copyrighted == True:
            ShellStats.CopyrightText = f"""Copyright (c) 2023 {ShellStats.Producer}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
            print(ShellStats.CopyrightText)
        PyConsole().cmdloop()

run()
