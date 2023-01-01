
import customtkinter
import os
from PIL import Image
from config import Settings

from controllers.file_uploader import FileUploader
from providers.googler import GoogleJobBank
from providers.splasher import Splasher
from tkinter import filedialog
# webbrowser
import webbrowser

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.file_uploader = FileUploader()
        self.google_job_bank = GoogleJobBank()
        self.splasher = Splasher()

        self.title(f"{self.settings.PROJECT_NAME} - {self.settings.TITLE}")
        self.geometry(f"{self.settings.WIDTH}x{self.settings.HEIGHT}")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../test/manual_integration_tests/test_images")
        self.logo_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
            size=(26, 26)
        )
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "large_test_image.png")),
            size=(500, 150)
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light.png")),
            size=(20, 20)
        )
        self.home_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "home_light.png")),
            size=(20, 20)
        )
        self.chat_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "saved.jpg")),
            dark_image=Image.open(os.path.join(image_path, "saved.jpg")),
            size=(20, 20)
        )
        self.jobs_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "jobs.png")),
            dark_image=Image.open(os.path.join(image_path, "jobs.png")),
            size=(20, 20)
        )
        self.favorite_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "fav.jpg")),
            dark_image=Image.open(os.path.join(image_path, "fav.jpg")),
            size=(20, 20)
        )

        # create navigation frame   
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text=f"  {self.settings.TITLE}", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # home button
        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        # skills frame
        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Skills",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.chat_image, anchor="w", command=self.frame_2_button_event
        )
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        # jobs frame
        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Jobs",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.jobs_image, anchor="w", command=self.frame_3_button_event
        )
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # favorites frame
        self.frame_4_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Favorites",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.favorite_image, anchor="w", command=self.frame_4_button_event
        )
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # upload cv button
        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame,
            text="Upload Resume",
            image=self.image_icon_image,
            compound="top",
            command=self.upload_cv_button_event
        )
        # let's put it the bottom right corner of the full window
        self.home_frame_button_3.place(relx=1, rely=1, x=-20, y=-20, anchor="se")
        
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "skills" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "jobs" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "favorites" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "skills":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "jobs":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "favorites":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
    
    # ------------------------------ events ------------------------------ # 
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("skills")

    def frame_3_button_event(self):
        self.select_frame_by_name("jobs")

    def frame_4_button_event(self):
        self.select_frame_by_name("favorites")

    def upload_cv_button_event(self):
        # open file dialog and allow user to select a file with pdf extension
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        skills = self.file_uploader.parse_skills(file_path=file_path)
        # now show these skills on the screen in a list of buttons
        self.show_skills(skills)

    def skill_button_event(self, skill):
        jobs = self.google_job_bank.fetch_jobs(skill)
        # now show these jobs on the screen in a list of buttons
        self.show_jobs(jobs)

    # ------------------------------ Renders ------------------------------ #
    def show_skills(self, skills):
        print("show skills")
        # remove all previous widgets
        for widget in self.second_frame.winfo_children():
            widget.destroy()

        # add a header saying choose your skills
        customtkinter.CTkLabel(self.second_frame, text="Choose your skills", font=customtkinter.CTkFont(size=15, weight="bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        # make skills a list of lists each containing 6 skills
        skills = [skills[i:i + 6] for i in range(0, len(skills), 6)]

        # create a list of buttons
        for skill in skills:
            for i in range(len(skill)):
                skill[i] = customtkinter.CTkButton(
                    self.second_frame,
                    text=skill[i],
                    compound="top",
                    command=lambda skill=skill[i]: self.skill_button_event(skill)
                )
                # show it under the header
                skill[i].grid(row=skills.index(skill) + 1, column=i, padx=20, pady=10)
        # open the second frame
        self.select_frame_by_name("skills")

    def show_jobs(self, jobs):
        print("show jobs : ", len(jobs))
        # remove all previous widgets
        for widget in self.third_frame.winfo_children():
            widget.destroy()

        # add a header saying choose your skills
        customtkinter.CTkLabel(self.third_frame, text="Choose your job", font=customtkinter.CTkFont(size=15, weight="bold")).grid(row=0, column=0, columnspan=4, padx=20, pady=10)

        # make jobs a list of lists each containing 2 jobs
        jobs = [jobs[i:i + 2] for i in range(0, len(jobs), 2)]

        # create a list of buttons
        for job in jobs:
            for i in range(len(job)):
                job[i] = customtkinter.CTkButton(
                    self.third_frame,
                    text=job[i].get("title"),
                    compound="top",
                    # just open the link in the browser
                    command=lambda job=job[i]: webbrowser.open(job.get("apply_url"))
                )
                # show it under the header
                job[i].grid(row=jobs.index(job) + 1, column=i, padx=20, pady=10)
        # open the third frame
        self.select_frame_by_name("jobs")



    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


