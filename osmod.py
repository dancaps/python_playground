#! python2
from subprocess import check_output

def get_disk():
    string_info = check_output("wmic logicaldisk get size,freespace,caption", shell=True)
    list_of_lines = string_info.split('\n')
    disk_info = []
    for i in list_of_lines:
        line = i
        caption_pos = line.find(' ')
        caption = line[:caption_pos]
        line = line[caption_pos + 1:]
        line = line.lstrip()
        free_pos = line.find(' ')
        free = line[:free_pos]
        line = line[free_pos + 1:]
        line = line.lstrip()
        size_pos = line.find(' ')
        size = line[:size_pos]
        if caption == 'Caption' or caption == ' ' or size == '' or free == '':
            continue
        elif caption == '\r' or size == '\r' or free == '\r':
            continue
        else:
            disk_info.append([caption, int(size) /1024 /1024 /1024, int(free) /1024 /1024 /1024])
    return disk_info

def low_disk(disk_info):
    ten_percent = disk_info[1] * .1
    if disk_info[2] <= ten_percent:
        return True
    else:
        return False

my_disks = get_disk()

for d in my_disks:
    print 'Partition:', d[0]
    if low_disk(d) == True:
        print 'This disk is low on freespace:', str(d[2]) + 'GB\n'
    else:
        print 'There is more than 10% freespace', str(d[2]) + 'GB\n'
