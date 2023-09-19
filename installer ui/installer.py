import os
import subprocess
from distutils.spawn import find_executable
from zipfile import ZipFile
import requests
import customtkinter as ctk

# links & misc
latest64win = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
latestRepo = "https://github.com/Legenden84/perlego-downloader_fork/archive/refs/heads/main.zip"
repoFileName = "perlego-downloader_fork-main"

def checkPythonInstall():
    try:
        a = subprocess.run('python --version', stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
        a = "".join(a.splitlines())
        return { "i": "Found " + a, "extended": a }
    except OSError:
        # incase python isn't installed
        return { "i": "Couldn't find a version of Python. Attempt download?", "try": "true" }
    except subprocess.CalledProcessError:
        # incase python returns a non-zero exit code (2), might be corrupt
        return { "i": "Python install might be corrupt" }

def onStart():
# BEGINNING OF STEPS:
    # - STEP 1
    def jumpStart():
        # commons
        pythonCheck = checkPythonInstall()
        logToScreen(pythonCheck["i"])
        if('try' in pythonCheck):
            global yesButton
            global noButton
            yesButton = ctk.CTkButton(root, text="Yes", width=250, height=30, command=attemptPythonInstall)
            yesButton.pack(padx=3,side="left",anchor='e', expand=True)
            noButton = ctk.CTkButton(root, text="No", width=250, height=30, fg_color="darkgray", hover_color="gray", command=getGit())
            noButton.pack(side="right",anchor='w',  expand=True)
        else: 
            getGit()
       # if('extended' in pythonCheck):
       #     if(pythonCheck["extended"].split()[1] <= "3.10.11"):
       #         return print("good to go!")
       #     if(pythonCheck["extended"].split()[1] < "3.6.0"):
       #         return print("not okay!")

#############################################################################################

    # - STEP 2
    def attemptPythonInstall():
        try:
            print("attempting an install...")
            req = requests.get(latest64win, allow_redirects=True)
            file = open('pythonInstaller.exe', 'wb').write(req.content)
            os.startfile(os.getcwd() + "\pythonInstaller.exe") # !! windows ONLY !!
            # by this point, we're assuming everything went okay,
            # and that we should continue with the installtion
            progressbar.step()
            noButton.destroy()
            yesButton.destroy()
            logToScreen("Downloaded Python 3.10.0\nFollow setup steps to continue\n ⚠️ (install to PATH) ⚠️")
            trackInstallation()
        except OSError as e:
            return print(e)
        except AttributeError as e:
            return print(e)
        
    # CONTINUATION

    # - STEP 2.1
    def trackInstallation():
        logToScreen("You can override this if the next step wasn't taken automatically")
        yesButton = ctk.CTkButton(root, text="Override", width=250, height=30, command=getGit, fg_color="darkred", hover_color="red")
        yesButton.pack(pady=20)
        while(find_executable("python") is not None):
             yesButton.destroy()
             print("Python installation was completed!")
             logToScreen("Python seems to be installed!\nNow downloading the repo...")
             return getGit()
             # return print("Python installation was completed!")
#############################################################################################

    # - STEP 3
    def getGit():
        progressbar.step()
        req = requests.get(latestRepo, allow_redirects=True)
        file = open('repo.zip', 'wb').write(req.content)
        progressbar.configure(mode="determinate", determinate_speed=1, progress_color="blue")
        progressbar.start()
        if(os.path.exists("repo.zip")):
            progressbar.stop()
            logToScreen("Unzipping repo...")
            progressbar.configure(mode="indeterminate", progress_color="light gray")
            progressbar.start()
            with ZipFile(os.getcwd() + "\\repo.zip", 'r') as zObject:
                zObject.extractall()
            zObject.close()
            os.remove("repo.zip")
            installReqs()
#############################################################################################

    # - STEP 4 
    def installReqs():
        logToScreen("Installing requirements.txt")
        # change current working directory
        os.chdir(os.getcwd() + "\\" + repoFileName)
        try:
            a = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
            print(a)
            print("we should be done!")
            logToScreen("Done")
            progressbar.configure(mode="determinate", progress_color="green")
            progressbar.stop()
            progressbar.set(1)
        except Exception as err:
            print(err)
        #finally:
           # os.rename(os.getcwd(), "perlego-downloader")
            #logToScreen(err)

#############################################################################################
    # UTIL 1
    def clearUI():
        # progressbar.step()
        title_label.destroy()
        desc.destroy()
        add_button.destroy()
#############################################################################################
    # UTIL 2
    def beginInstaller():
        progressbar.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        progressbar.pack(side="bottom", pady = 10, padx = 1.5)

    # set the bar to zero so it doesn't default to 50% 
        progressbar.set(0)
        clearUI()
        progressbar.step()
        jumpStart()
#############################################################################################
    # UTIL 3
    def logToScreen(log):
        desc  = ctk.CTkLabel(root, text=log, font=ctk.CTkFont(size=20, weight="normal"))
        desc.pack(padx=5, pady=3)
##############################################################################################

# Main UI starters
    root = ctk.CTk()
    root.geometry("750x450")
    root.title("Quick Install")
    # root.iconbitmap("./favicon.ico") not really needed

    title_label = ctk.CTkLabel(root, text="Install the required dependencies for perlego-downloader", font=ctk.CTkFont(size=25, weight="bold"))
    title_label.pack(padx=1, pady=(100, 20))

    desc  = ctk.CTkLabel(root, text="This will install the following:\n* Python 3.10\n* all required dependencies", font=ctk.CTkFont(size=20, weight="normal"))
    desc.pack(padx=5)

    add_button = ctk.CTkButton(root, text="🚀 Ready?", width=500, command=beginInstaller)
    add_button.pack(pady=20)

    global progressbar
    progressbar = ctk.CTkProgressBar(master=root,
                                           width=730,
                                           height=20,
                                           border_width=3,
                                           progress_color="light gray",
                                           )

    root.mainloop()

onStart()