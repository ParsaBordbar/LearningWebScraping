import requests
from bs4 import BeautifulSoup

url = 'https://fireship.io/courses'
response = requests.get(url)
print(response)

class Course:
    def __init__(self, courseName, courseTags):
        self.courseName = courseName
        self.courseTags = courseTags
    def stringify(self):
        return f'courseName: {self.courseName} courseTags: {self.courseTags}'
        
    
coursesList = []
  
soup = BeautifulSoup(response.text , 'html.parser')
courseDetails = soup.select('section')
for i in courseDetails:
    course = Course('', '')
    coursesNames = i.select('h5')
    for courseName in coursesNames:
        name = courseName.text.strip()
        course.courseName = name
        
    coursesTags = i.select('.tag')
    for courseTag in coursesTags:
        tags = []
        tags.append(courseTag.text.strip())
        course.courseTag = tags
    coursesList.append(course.stringify())
print(coursesList)