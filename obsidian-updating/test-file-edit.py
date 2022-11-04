import re
# File Objects

with open('test.md', 'r') as rf:
    with open('test2.md', 'w') as wf:
        lines = rf.readlines()

        inHeading = True
        isNote = False

        if (lines[1] != '\n'):
            isNote = True

        
        if isNote:
            # Update Heading
            topic = re.sub('[\[\]]', '', lines[5][8:]).replace(' ', '_')
            wf.write(lines[0])
            wf.write(lines[2])
            wf.write(f"Tags: #{topic}")
            
            # Write rest of file
            for 
            




        # for line in rf:

        #     if inHeading:
                
                

        #     if not (line != "\n" and counter == 1):
        #         f.write(line)
        #     counter += 1
