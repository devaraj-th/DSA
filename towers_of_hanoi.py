def towers_of_hanoi(number_of_disks,start=1,end=3):

    if number_of_disks:

        towers_of_hanoi(number_of_disks-1,start,6-start-end)
        print("move the disk %d from peg %d to peg %d" %(number_of_disks,start,end))

        towers_of_hanoi(number_of_disks-1,6-start-end,end)


towers_of_hanoi(number_of_disks=4)