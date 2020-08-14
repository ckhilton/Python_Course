#




def newPage():
    f = open('new_page.html','w')
    message = """<html>
    <body>
    Stay tuned for our amazing summer sale!
    </body>
    </html>"""

    f.write(message)
    f.close()


if __name__ == "__main__":
    newPage()
