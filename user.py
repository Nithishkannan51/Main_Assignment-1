from xlwt import Workbook
from xlrd import open_workbook as rd

from xlutils.copy import copy

class user():
    def __init__(self):
        self.RemainingSeats=0
        self.wb1=""
        self.w_sheet=""
        self.list1=""
        self.r=""
        self.s=""
        self.num=""
    def bookticket(self,num):
        print("booking ticket")
        self.r = rd("Movielist.xls")
        self.s = self.r.sheet_by_index(0)
        size_col = self.s.ncols
        size_row = self.s.nrows
        self.wb1 = copy(self.r)
        self.w_sheet = self.wb1.get_sheet(0)

        self.num=num
        print(self.num)
        timing=self.s.cell(7,self.num).value
        print("Timings available listed below for selected movie")
        list=timing.split(",")
        for i in range(len(list)):
            j=str(i+1)
            print(j+" :"+list[i])
        t=int(input("Select Timings: "))
        print("Timing selected: "+list[t-1])

        Seats= self.s.cell(12, self.num).value
        self.list1 = Seats.split(",")
        print("Remaining Seats: "+ self.list1[1])
        Bookseats=int(input("Enter Number of seats: "))
        if(Bookseats>int(self.list1[1])):
            print("Number given is more than remaining seats")
            Bookseats = int(input("Enter Number of seats: "))
        if(Bookseats<=0):
            print("Invalid number please give another number")
            Bookseats = int(input("Enter Number of seats: "))
        capacity=int(self.list1[1])

        self.RemainingSeats=capacity-Bookseats
        self.w_sheet.write(12, self.num, self.list1[0]+","+str(self.RemainingSeats))
        self.wb1.save('Movielist.xls')
        print("Thanks for booking. ")
    def cancelticket(self,num):
        print("cancel ticket")
        Cancelseat=int(input("Number of seats you want to cancel:"))

        self.num1=num
        self.r = rd("Movielist.xls")
        self.s = self.r.sheet_by_index(0)
        self.wb1 = copy(self.r)
        self.w_sheet = self.wb1.get_sheet(0)
        Seats = self.s.cell(12, self.num1).value
        self.list1 = Seats.split(",")
        self.RemainingSeats=int(self.list1[1])

        self.RemainingSeats= self.RemainingSeats+Cancelseat
        if(self.RemainingSeats>int(self.list1[0])):
            self.new_remaining=self.list1[0]
        else:
            self.new_remaining=str(self.RemainingSeats)
        #value=self.list1[0]+","+new_remaining

        self.w_sheet.write(12, self.num1, self.list1[0]+","+self.new_remaining)
        self.wb1.save('Movielist.xls')
        #cancel: 5
    def userrating(self):
        print("Please enter rating for the following movie out of 5: ")
        rating=input()

        print("User rating given for the movie is "+rating)







