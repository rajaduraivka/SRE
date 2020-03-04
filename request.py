import requests

url= 'https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/article_images/2019/11/13/kohli-1573662330.jpg?itok=EkUzIOII'

myfile = requests.get(url)

open('/Users/rajadurai/Durai/kohli.jpg','wb').write(myfile.content)
