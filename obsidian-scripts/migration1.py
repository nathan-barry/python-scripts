import os
import re

path = r'/home/anon/Notes/Zettelkasten'
dir_list = os.listdir(path)

for dir in dir_list:
    with open(path+'/'+dir, 'r') as rf:
        with open(f'/home/anon/Zettelkasten/{dir}', 'w') as wf:
            lines = rf.readlines()

            inHeading = True
            isNote = False

            if (lines[1] != '\n'):
                isNote = True

            
            if isNote:
                # Update Heading
                wf.write('---\n')
                title = lines[7][2:]
                wf.write(f"title: \"{title.strip()}\"\n")
                wf.write(f"date: \"{lines[0].strip()}\"\n")
                topic = re.sub('[\[\]]', '', lines[5][8:]).lower().replace(" ", "-")
                wf.write(f"tags: {topic}")
                wf.write("aliases: \n")
                wf.write('---\n')
                
                # Write rest of file
                for i in range(9, len(lines)):
                    wf.write(lines[i])
            else:
                # Write all
                for line in lines:
                    wf.write(line)
