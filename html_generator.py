def concept_read(lesson_text,list_of_contents):
    #count_concept = 0
    end_loc_lesson = lesson_text.find('''TITLE: ''')
    lesson = lesson_text[ 7:end_loc_lesson]
    while len(lesson_text) > 1:
        start_loc_concept = lesson_text.find('''TITLE: ''')
        next_loc_concept = lesson_text.find('''TITLE: ''', start_loc_concept + 1)
        start_loc_description = lesson_text.find('''DESCRIPTION: ''')
        concept = lesson_text[start_loc_concept+6:start_loc_description]
        if next_loc_concept == -1:
            description = lesson_text[start_loc_description+13:]
            lesson_text = ""
        else:
            description = lesson_text[start_loc_description+13:next_loc_concept]
            lesson_text = lesson_text[next_loc_concept:]

        list_of_contents.append([lesson, concept, description])
     
    return list_of_contents
        


def lesson_read(content_text,list_of_contents):
    #count_lesson = 0
    while len(content_text) > 1:
        start_loc_lesson = content_text.find('''LESSON: ''')
        next_loc_lesson = content_text.find('''LESSON: ''', start_loc_lesson +1)
        if next_loc_lesson == -1:
            lesson_current = content_text[start_loc_lesson:]
            content_text = ""
        else:
            lesson_current = content_text[start_loc_lesson:next_loc_lesson]
            content_text = content_text[next_loc_lesson: ]
        concept_read(lesson_current,list_of_contents)
        #print content_text
        
    return list_of_contents

list_of_contents = []
print list_of_contents
with open("Notes-ANSI.txt", "r") as that_file:
    example_context = that_file.read()
that_file.close


lesson_read(example_context,list_of_contents)

                                            
def generate_HTML(list_of_contents):
    #assign html header info to html_output
    html_output = '''
<!DOCTYPE html>
<html>
    <head> 
	<meta charset = "utf-8">
	<meta name = "viewport" content="width=device-width, initial-scale=1"> 
	<title>Lesson Notes</title>
	<link rel="stylesheet" href = "css/bootstrap.css">
	<link href="css/main.css" rel="stylesheet" type = "text/css">
    </head>
    <body>
        <div class="container" style = "outline: 5 px solid red;">
            <div class="row margin-bottom" style="display:flex; margin-bottom: 30px;">
                <div class="col-md-4"> <img class="img-responsive" src="images/logo.png" alt="log"></div>
                <div class="col-md-8 text-right"><H1 style="margin-bottom:30px;font-weight:550;">Introduction to Programming</H1><H3>Class Notes</H3></div>
            </div>'''
   
    i = 0
    temp_lesson = ""
    while i <= len(list_of_contents)-1:
        if list_of_contents[i][0] != temp_lesson:
            html_row_begin = '''
            <div class="row" style="display:flex;outline:5px solid red;margin-left:15px;margin-right:15px;margin-bottom:15px">'''
            html_lesson_begin = '''
                <div class="col-md-4 text-center"><H3 style="margin-bottom:30px;font-weight:550;">''' + list_of_contents[i][0] + '''
                                                  </H3>'''
            html_lesson_end = '''
                </div>'''
            html_title_begin = '''
                <div class="col-md-8 text-left">'''
            html_output = html_output + html_row_begin + html_lesson_begin+html_lesson_end+html_title_begin
        html_title = ""
        html_description = ""
        html_title = html_title + '''
                    <H3 class="subtitle">''' + list_of_contents[i][1] + '''
                    </H3>'''
        html_description= html_description + '''
                    <H4 class="textfile">''' + list_of_contents[i][2] + '''
                    </H4>'''
        html_output = html_output + html_title + html_description
        if (i < len(list_of_contents) - 1) and (list_of_contents[i][0] != list_of_contents[i+1][0]):
            html_title_end = '''
                </div>'''
            html_row_end = '''
            </div>'''
            html_output = html_output + html_title_end + html_row_end
        if i == len(list_of_contents)-1:
            html_title_end = '''
                </div>'''
            html_row_end = '''
            </div>'''
            html_output = html_output + html_title_end + html_row_end
        temp_lesson = list_of_contents[i][0]
        i = i + 1
    html_output = html_output + '''
        </div>
    </body>
</html>'''
    return html_output
                
#print generate_HTML(list_of_contents)
html_output = generate_HTML(list_of_contents)
print html_output
with open("autohtml.html","w") as the_file:
    the_file.write(html_output)
the_file.close
