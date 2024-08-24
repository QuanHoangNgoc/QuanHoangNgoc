import requests
from requests.auth import HTTPBasicAuth
import os


# Replace these with your own values
username = "@QuanHoangNgoc"
token = os.getenv("GITHUB_TOKEN")
repo_name = username  # For the special GitHub Profile README repo

if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is not set.")


# Function to get all repositories
def get_all_repos(username, token):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        response = requests.get(url, auth=HTTPBasicAuth(username, token))
        if response.status_code == 200:
            repos_page = response.json()
            if not repos_page:
                break
            repos.extend(repos_page)
            page += 1
        else:
            print(f"Failed to fetch repositories: {response.status_code}")
            break
    return repos


# Function to get traffic data (views, clones) for a specific repository
def get_traffic_data(url, username, token):
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    if response.status_code == 200:
        data = response.json()
        return data.get("count", 0), data.get("uniques", 0)
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return -1, -1


# Function to get stars count for a specific repository
def get_stars_count(repo):
    return repo.get("stargazers_count", 0)


########################################################################
# Initialize total counters
total_views = 0
total_clones = 0
total_stars = 0

# Fetch all repositories
repositories = get_all_repos(username, token)

# Iterate over each repository to sum up views, clones, and stars
for repo in repositories:
    repo_name = repo["name"]
    owner = repo["owner"]["login"]

    # URLs for traffic data
    views_url = f"https://api.github.com/repos/{owner}/{repo_name}/traffic/views"
    clones_url = f"https://api.github.com/repos/{owner}/{repo_name}/traffic/clones"

    # Get and sum views
    repo_views, _ = get_traffic_data(views_url, username, token)
    total_views += repo_views

    # Get and sum clones
    repo_clones, _ = get_traffic_data(clones_url, username, token)
    total_clones += repo_clones

    # Get and sum stars
    total_stars += get_stars_count(repo)

    print(
        f"Updated README.md with totals: Views: {total_views}, Clones: {total_clones}, Stars: {total_stars}"
    )


# Update the README.md file
readme_content = f"""

<h1 align="center">Hi 👋, I'm Quan-Hoang-Ngoc</h1>
<h3 align="center">Scholar at the University of Information Technology (UIT) in Ho Chi Minh City, Vietnam</h3>

---

I'm a passionate scholar at the University of Information Technology (UIT) in Ho Chi Minh City, Vietnam. My interests span across **mindset development** and **computer science**, where I enjoy diving deep into research and development. I'm always eager to learn and collaborate on exciting projects, especially in the realms of data science, machine learning, and software development.

- 🌱 Currently exploring advanced concepts in computer science.
- 🔭 Actively contributing to open-source projects on [GitHub](https://github.com/QuanHoangNgoc).
- 📚 Sharing knowledge through **[Articles](https://sites.google.com/view/quan12i/trang-ch%E1%BB%A7?fbclid=IwAR3FfEwShxH6ZSOuZovAmZRb5TsljtnbunuYTHFITcd_K4odDwrVUyzzvjQ) and [YouTube](https://www.youtube.com/@QuanHoangNgoc-yu9uo?sub_confirmation=1)**.

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/quanhoangngoc) or check out my work on [Kaggle](https://www.kaggle.com/quanhoangngoc).

---

<p align="center">
   <img src="https://komarev.com/ghpvc/?username=quanhoangngoc&label=Profile%20views&color=0e75b6&style=flat" alt="Profile Views" />
</p>

<p align="center">
   <a href="https://github.com/ryo-ma/github-profile-trophy">
      <img src="https://github-profile-trophy.vercel.app/?username=quanhoangngoc" alt="GitHub Trophies" />
   </a>
</p>

---

### 👨‍💻 About Me:
- 🔭 Currently studying at **University of Information Technology (UIT)**
- 🌱 Learning **Mindset and Computer Science**
- 👯 Looking to collaborate on [Kaggle](https://www.kaggle.com/quanhoangngoc)
- 🤝 Seeking assistance with my **[YouTube Channel](https://www.youtube.com/@QuanHoangNgoc-yu9uo?sub_confirmation=1)**
- 📝 Writing articles on [Quan_2022_ago](https://sites.google.com/view/quan12i/trang-ch%E1%BB%A7?fbclid=IwAR3FfEwShxH6ZSOuZovAmZRb5TsljtnbunuYTHFITcd_K4odDwrVUyzzvjQ)
- 💬 Ask me about **Research and Development**
- 📫 Reach me on [Facebook](https://www.facebook.com/quanhnqt)
- 📄 Learn more about my experiences on [LinkedIn](https://www.linkedin.com/in/quanhoangngoc)
- ⚡ Fun fact: [Quan's Fun Facts](https://sites.google.com/view/hoangngocquan/home?fbclid=IwAR19-OvVtYz1TaMStSQ_BrDJ4g3rshGup14P3GR1ri77oQe2_XzvLwBVDis)

---

### 🌐 Connect with Me:
<p align="center">
   <a href="https://www.linkedin.com/in/quanhoangngoc" target="_blank">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
   </a>
   <a href="https://www.kaggle.com/quanhoangngoc" target="_blank">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="Kaggle" height="30" width="40" />
   </a>
   <a href="https://www.facebook.com/quanhnqt" target="_blank">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
   </a>
   <a href="https://www.youtube.com/@QuanHoangNgoc-yu9uo?sub_confirmation=1" target="_blank">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="YouTube" height="30" width="40" />
   </a>
   <a href="https://codeforces.com/profile/quanhn" target="_blank">
      <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/codeforces.svg" alt="Codeforces" height="30" width="40" />
   </a>
</p>

---

### 🛠 Languages and Tools:
<p align="center">
   <a href="https://www.w3schools.com/cpp/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="C++" width="40" height="40"/>
   </a>
   <a href="https://www.w3schools.com/cs/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="C#" width="40" height="40"/>
   </a>
   <a href="https://dotnet.microsoft.com/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dot-net/dot-net-original-wordmark.svg" alt=".NET" width="40" height="40"/>
   </a>
   <a href="https://flask.palletsprojects.com/" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="Flask" width="40" height="40"/>
   </a>
   <a href="https://flutter.dev" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/flutterio/flutterio-icon.svg" alt="Flutter" width="40" height="40"/>
   </a>
   <a href="https://git-scm.com/" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" width="40" height="40"/>
   </a>
   <a href="https://www.java.com" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="Java" width="40" height="40"/>
   </a>
   <a href="https://www.linux.org/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="Linux" width="40" height="40"/>
   </a>
   <a href="https://www.microsoft.com/en-us/sql-server" target="_blank">
      <img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="SQL Server" width="40" height="40"/>
   </a>
   <a href="https://www.mysql.com/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="MySQL" width="40" height="40"/>
   </a>
   <a href="https://opencv.org/" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="OpenCV" width="40" height="40"/>
   </a>
   <a href="https://pandas.pydata.org/" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="Pandas" width="40" height="40"/>
   </a>
   <a href="https://www.python.org" target="_blank">
      <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/>
   </a>
   <a href="https://pytorch.org/" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="PyTorch" width="40" height="40"/>
   </a>
   <a href="https://scikit-learn.org/" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-Learn" width="40" height="40"/>
   </a>
   <a href="https://seaborn.pydata.org/" target="_blank">
      <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="Seaborn" width="40" height="40"/>
   </a>
   <a href="https://www.sqlite.org/" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="SQLite" width="40" height="40"/>
   </a>
   <a href="https://www.tensorflow.org" target="_blank">
      <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="TensorFlow" width="40" height="40"/>
   </a>
</p>

---

### 💖 Support:
<p align="center">
   <a href="https://www.buymeacoffee.com/https://www.youtube.com/@QuanHoangNgoc-yu9uo">
      <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="Buy Me A Coffee" />
   </a>
</p>
Buy me a coffee by star for my projects and like for my YouTube videos. Thank you so much! 

---

### 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=quanhoangngoc&show_icons=true&theme=radical&hide_border=true" alt="Quan-Hoang-Ngoc's GitHub Stats" />
</p>

<!---
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=quanhoangngoc&theme=radical&hide_border=false" alt="Quan-Hoang-Ngoc's GitHub Streak" />
</p>
---> 

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=quanhoangngoc&layout=compact&theme=radical&hide_border=true" alt="Top Languages" />
</p>

---

### 📂 My Repositories

<p align="center">
  <a href="https://github.com/QuanHoangNgoc/CoffeeShopManagementApp">
    <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/QuanHoangNgoc/Coffee-Shop-Management-App-SE-&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=views&edge_flat=false" alt="Views" />
    <img src="https://img.shields.io/github/stars/QuanHoangNgoc/Coffee-Shop-Management-App-SE-?style=social" alt="Stars" />
    <img src="https://img.shields.io/github/forks/QuanHoangNgoc/Coffee-Shop-Management-App-SE-?style=social" alt="Forks" />
  </a>
  <br>
  <a href="https://github.com/QuanHoangNgoc/Coffee-Shop-Management-App-SE-"><b>Coffee Shop Management App</b></a>
  <p>A robust local device app to revolutionize coffee shop management, built with C#, SQL Server, and OOP design principles.</p>
</p>


---
## 🌟 Quan-Hoang-Ngoc's GitHub Profile 🌟

Welcome to my GitHub profile! I'm passionate about open-source development, research, and building innovative solutions. Here you can find some insights into the activity across all my repositories.

### 📊 GitHub Repository Metrics

![Views](https://img.shields.io/badge/Views-{total_views}-blue?style=flat-square)
![Clones](https://img.shields.io/badge/Clones-{total_clones}-green?style=flat-square)
![Stars](https://img.shields.io/badge/Stars-{total_stars}-yellow?style=flat-square)

| Metric        | Total Count |
|---------------|-------------|
| **🔍 Total Views**   | {total_views}     |
| **🔄 Total Clones**  | {total_clones}    |
| **⭐ Total Stars**   | {total_stars}     |

*These stats are automatically updated using a GitHub Action.*
---

"""


########################################################################
# Write to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)


########################################################################
