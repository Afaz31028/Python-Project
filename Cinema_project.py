class Star_Cinema:
    __hall_list=[]

    def entry_hall(self,obj):
        Star_Cinema.__hall_list.append(obj)
    
    def get_list():
            return Star_Cinema.__hall_list
        
    def set_list(self,obj):
        Star_Cinema.__hall_list.append(obj)

class Hall(Star_Cinema):
    def __init__(self,rows,columns,hall_no):
        self.rows=rows
        self.columns=columns
        self.hall_no=hall_no
        self.seats={}
        self.__show_list=[]
        self.set_list(self)

    def get_show_list(self):
        return self.__show_list
    
    def set_show_list(self,obj):
        self.__show_list.append(obj)
    
    def entry_show(self,id,movie_name,time):
        hall=(id,movie_name,time)
        self.set_show_list(hall)
        array = [['0' for _ in range(self.columns)] for _ in range(self.rows)]
        self.seats[id]=array
    
    def book_seats(self,id,Seat_pos):
        x=self.seats[id]
        booked_seat=[]
        if id not in self.seats:
            print('\tThe movie is not showing')
        else:
            for row,col in Seat_pos:
                if 0<=row<self.rows and 0<=col< self.columns:
                    if x[row][col]=='0':
                        x[row][col]='B'
                        booked_seat.append(f'The seat no. R{row+1}C{col+1} is successfully booked')
                    else:
                        booked_seat.append(f'The seat no. R{row+1}C{col+1} is alradey booked, Try the other one')
                else:
                    booked_seat.append(f"The seat no. R{row+1}C{col+1} is Invalid!")
        self.seats[id] = x
        if len(booked_seat)>0 :
            return "\n".join(booked_seat)

    def view_show_list(self):
        for show in self.get_show_list():
            print(f'[Movie ID:{show[0]}] [Movie Name:{show[1]}] [Time:{show[2]}]')
        print("")
        
    def view_available_seats(self,id):
        y=self.seats[id]
        if id not in self.seats:
            print("The show is not running")
        else:
            print(f'    The seats of show Id {id}')
            for i in range(len(y)):
                for j in range(len(y[i])):
                    print("  ",y[i][j],end=" ")
                print("")
            print("")

h1 = Hall(5, 5, "Hall-1")
h2 = Hall(4, 5, "Hall-2")

h1.entry_show("A1", "Brother", "5:00PM")
h1.entry_show("M5", "Lucky Buskhar", "11:00AM")
h2.entry_show("B3", "Toofan", "2:00PM")

print("-----------Welcome------------")
flag=True
while(flag):

    print("***********OPTIONS**************")
    print("  1. Show Hall List")
    print("  2. Show Avilable Seats")
    print("  3. Ticket Booked")
    print("  4. Exit")
    op=int(input("\tChoose an option:"))
    if op==1:
        if len(Star_Cinema.get_list())==0:
            print("")
            print("\tThere is no movie shows in any Hall!!!\n")
        else:    
            for item in Star_Cinema.get_list():
                print('')
                print(f'\tHall:{item.hall_no}')
                item.view_show_list()
    elif op==2:
        ID=input("\tEnter Show ID:")
        for item in Star_Cinema.get_list():
            if ID in item.seats:
                item.view_available_seats(ID)
                break
        else:
            print(f"   Show ID: {ID} is not found.\n")
    elif op==3:
        ID=input("\tEnter Show ID:")
        NoOfSeat=int(input("\tHow much tickets do you need: "))
        SeatPos=[]
        for i in range(NoOfSeat):
            x,y=map(int,input("\tEnter seat's row and column No: ").split())
            SeatPos.append((x-1,y-1))
        for item in Star_Cinema.get_list():
            if ID in item.seats:
                message=item.book_seats(ID,SeatPos)
                print("Cofirmation Message:")
                print(message)
                print("")
                break
    elif op==4:
        flag=False
        print("-----------Thank You------------")
    else:
        print("   You chose an invalid option")
        print("       Try Again!\n")
