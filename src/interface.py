from src import customerManager
from src import masseuseManager
from src import appointmentManager
from src import availabilityManager
from src import mysqlManager
import random
from datetime import datetime, timedelta, date


"""
This is almost a read me file
I'm listing all methods that control the MySQL database. 
I'm also listing every function call I used
to create what's in the database 

James

"""

# Gather info from user to create a new customer
"""customerManager.insert_customer(customerId,name,address,email,phone)"""

# Gather info from user to create a new masseuse
"""masseuseManager.insert_masseuse(masseuseId,name,address,email,phone)"""

# Gather info from user About a masseuse
# Note: 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.
# Go through each week day (int, 2 – 6), 
# ask for start time (int, 0 – 23), end time (int, 0 – 23), or skip day of the week
# end time > start time
"""availabilityManager.insert_availability(masseuseId,dow,start,end)"""

"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
I do not think that this is a good idea
I put it in at the beginning, but it doesn't 
make any sense to have empty appointments

Populate empty appointments let's say 8 weeks out
8 start times should be created for each day (9a to 5p)
each start time should have 3 rooms
this creates empty appointments with status OPEN
"""

# insert_appointment(start_time,room,status,masseuseId,customerId)
"""appointmentManager.insert_appointment(start_time,room,"OPEN",NULL,NULL)"""

# Use to book or cancel appointment
# update_appointment(appointmentId,status,masseuseId,customerId)
"""appointmentManager.update_appointment(appointmentId,"BOOKED",masseuseId,customerId)"""
    # Cancel APPT
"""appointmentManager.update_appointment(appointmentId,"OPEN",NULL,NULL)"""

# ! This might logically be the start (when you open the program)
# ask customer which day they want to book/cancel
# Returns all appointments for that day (each hour, each room)
"""appointmentManager.get_appointments(date)"""

# returns array of masseuseId that are available for each appointment
"""availabilityManager.get_availability(start_time)"""
# if(empty)
#   start_time does not have any available masseuses

# to display names use
"""customerManager.get_customer_name(customerId)"""
"""masseuseManager.get_masseuse_name(masseuseId)"""



"""
I used the following code to insert fake customers and masseuse

35 customers
15 masseuse
then, I used the masseuseIDs generated to insert availability
all 15 masseuse are available to work
    Monday – Friday (represented as integers 2 – 6)
    9am - 5pm (represented as integers 9 - 16)
    
4 appointments added

!! I did not do these 3 checks, but in the future these are important !!
    need to check if appointment exists already in that room at that hour
    need to check masseuse/customer are already scheduled at this hour
    need to check if masseuse has availability at that hour, on that day

appointmentManager.insert_appointment('2022-10-06 15:00:00',1,'BOOKED',13741,10325)
appointmentManager.insert_appointment('2022-10-06 18:00:00',1,'BOOKED',13741,10325)
appointmentManager.insert_appointment('2022-12-06 17:00:00',1,'BOOKED',13741,10325)
appointmentManager.insert_appointment('2022-12-06 18:00:00',1,'BOOKED',13741,10325)

customerManager.insert_customer(random.randint(10000, 99999),'Margret Howell ','5 Albany Ave.Windermere, FL 34786 ','fragileRonald@aol.com ','(894) 404-9598 ')
customerManager.insert_customer(random.randint(10000, 99999),'Maxwell Ortiz ','20 North Corona RoadSouth Richmond Hill, NY 11419 ','goodTamara52@sky.com ','(903) 538-4872 ')
customerManager.insert_customer(random.randint(10000, 99999),'Norbert Gunn DDS ','916 Peninsula St.Endicott, NY 13760 ','amusedArthur@neuf.fr ','(214) 208-9729 ')
customerManager.insert_customer(random.randint(10000, 99999),'Tyrique Gleason ','9111 S. Harvey AvenueWantagh, NY 11793 ','Denisetough@ntlworld.com ','(287) 285-1053 ')
customerManager.insert_customer(random.randint(10000, 99999),'Tia Hane ','916 Peninsula St.Endicott, NY 13760 ','Monicaamused@frontiernet.net ','(219) 262-7798 ')
customerManager.insert_customer(random.randint(10000, 99999),'Alejandrin Kovacek ','9111 S. Harvey AvenueWantagh, NY 11793 ','goodEbony61@frontiernet.net ','(440) 323-3791 ')
customerManager.insert_customer(random.randint(10000, 99999),'Johnny Waters ','294 Thatcher CourtBrockton, MA 02301 ','pleasantPatricia62@aim.com ','(753) 923-3627 ')
customerManager.insert_customer(random.randint(10000, 99999),'Bernie Zboncak ','720 River StreetUtica, NY 13501 ','hungryLuke27@chello.nl ','(340) 421-4350 ')
customerManager.insert_customer(random.randint(10000, 99999),'Miss Madie Kilback ','294 Thatcher CourtBrockton, MA 02301 ','Curtisshiny@tiscali.it ','(808) 201-6074 ')
customerManager.insert_customer(random.randint(10000, 99999),'Kurtis Ryan ','720 River StreetUtica, NY 13501 ','cheerfulTamara7@yahoo.in ','(224) 467-7709 ')
customerManager.insert_customer(random.randint(10000, 99999),'Miss Marlee Harber ','8033 Rockwell StreetGainesville, VA 20155 ','gracefulDesiree62@ig.com.br ','(559) 684-0494 ')
customerManager.insert_customer(random.randint(10000, 99999),'Lorenza Robel ','60 Lancaster Ave.Sicklerville, NJ 08081 ','Melissabored@tiscali.co.uk ','(929) 255-6825 ')
customerManager.insert_customer(random.randint(10000, 99999),'Filiberto Ankunding ','8033 Rockwell StreetGainesville, VA 20155 ','joyousRaquel@live.ca ','(846) 397-4832 ')
customerManager.insert_customer(random.randint(10000, 99999),'Jackson Moore ','60 Lancaster Ave.Sicklerville, NJ 08081 ','Cindylonely@skynet.be ','(237) 276-8986 ')
customerManager.insert_customer(random.randint(10000, 99999),'Opal Abbott Sr. ','508 Tanglewood LanePhoenix, AZ 85021 ','thoughtfulCorey67@live.com.au ','(551) 262-3754 ')
customerManager.insert_customer(random.randint(10000, 99999),'Akeem Becker ','897 Deerfield St.Mableton, GA 30126 ','Rickyfantastic@bol.com.br ','(661) 646-2142 ')
customerManager.insert_customer(random.randint(10000, 99999),'Rod Halvorson ','508 Tanglewood LanePhoenix, AZ 85021 ','richJenny71@chello.nl ','(928) 661-7197 ')
customerManager.insert_customer(random.randint(10000, 99999),'Haleigh Schmeler ','Phoenix, AZ 85021897 Deerfield St. ','aggressiveHolly59@charter.net ','(597) 919-2502 ')
customerManager.insert_customer(random.randint(10000, 99999),'Leanna Larson ','Mableton, GA 30126517 W. York Lane ','worriedChristina@live.com.au ','(754) 854-1761 ')
customerManager.insert_customer(random.randint(10000, 99999),'Dakota Schuster III ','Stamford, CT 069027989 E. Rockaway Street ','smilingNancy@live.com ','(645) 398-3478 ')
customerManager.insert_customer(random.randint(10000, 99999),'Mr. Pasquale Reichert ','Crawfordsville, IN 479337 Anderson Court ','Erikahappy@live.com ','(971) 915-9606 ')
customerManager.insert_customer(random.randint(10000, 99999),'Camilla Schowalter MD ','Stamford, CT 069027989 E. Rockaway Street ','unusualCameron36@t-online.de ','(672) 866-5521 ')
customerManager.insert_customer(random.randint(10000, 99999),'Miss Osborne Marks ','Crawfordsville, IN 479337 Anderson Court ','Karenawful@yahoo.co.uk ','(264) 777-6518 ')
customerManager.insert_customer(random.randint(10000, 99999),'Verona Lehner ','Ossining, NY 10562259 Wayne Rd. ','Fernandocareful@live.ca ','(443) 593-3599 ')
customerManager.insert_customer(random.randint(10000, 99999),'Dr. Hilda Gislason ','Gloucester, MA 01930183 Lafayette Court ','Matthewpoised@me.com ','(565) 639-9418 ')
customerManager.insert_customer(random.randint(10000, 99999),'Miss Orville Morissette ','Ossining, NY 10562259 Wayne Rd. ','carefulMario67@hetnet.nl ','(410) 988-4214 ')
customerManager.insert_customer(random.randint(10000, 99999),'Bernita Koch ','Gloucester, MA 01930183 Lafayette Court ','fancyJames@aol.com ','(896) 361-3792 ')
customerManager.insert_customer(random.randint(10000, 99999),'Ms. Melyna Miller ','Winter Haven, FL 338807007 Bayberry Drive ','zealousMichelle84@ig.com.br ','(354) 897-5306 ')
customerManager.insert_customer(random.randint(10000, 99999),'Emmie Lehner ','Dallas, GA 301327109 Jones St. ','fancyRaquel72@mail.com ','(397) 546-0896 ')
customerManager.insert_customer(random.randint(10000, 99999),'Laron Torp ','Winter Haven, FL 338807007 Bayberry Drive ','fragileAngela10@aliceadsl.fr ','(785) 311-1550 ')
customerManager.insert_customer(random.randint(10000, 99999),'Mr. Kirk Feest ','Dallas, GA 301327109 Jones St. ','Mayradifferent@yahoo.ca ','(733) 400-4074 ')
customerManager.insert_customer(random.randint(10000, 99999),'Christa Gaylord ','Fall River, MA 02720480 Gulf St. ','adorableJohn1@tiscali.co.uk ','(697) 733-5756 ')
customerManager.insert_customer(random.randint(10000, 99999),'Elbert Nicolas II ','Camas, WA 986077566 East Wall St. ','Terrancelong@yahoo.com ','(446) 713-0701 ')
customerManager.insert_customer(random.randint(10000, 99999),'Ms. Holly Schmeler ','Fall River, MA 02720480 Gulf St. ','importantBrianna66@skynet.be ','(725) 438-3442 ')
customerManager.insert_customer(random.randint(10000, 99999),'Garrett Cremin ','480 Gulf St.Camas, WA 98607 ','naughtyEddie@aol.com ','(935) 433-2881 ')

masseuseManager.insert_masseuse(random.randint(10000, 99999),'Michel Hilll IV ','7566 East Wall St.Longview, TX 75604 ','Armandofriendly@tin.it ','(752) 350-6308 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Gus Pagac ','19 South Bishop AvenueEncino, CA 91316 ','Kevindisturbed@yandex.ru ','(946) 551-1084 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Mrs. Cara Marks ','26 SE. Bridle CourtMaineville, OH 45039 ','Summermushy@telenet.be ','(427) 369-5342 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Mrs. Kathryn Kuhic ','19 South Bishop AvenueEncino, CA 91316 ','enviousDawn@googlemail.com ','(792) 648-0614 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Brianne McCullough ','26 SE. Bridle CourtMaineville, OH 45039 ','foolishCrystal@arcor.de ','(287) 561-4123 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Emmie Parker ','204 North Border St.Pelham, AL 35124 ','powerfulTiffany@cox.net ','(306) 664-9880 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Nyasia Considine DVM ','7639 Oak CourtBluffton, SC 29910 ','disturbedLeonard@live.com ','(850) 717-1766 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Florence Metz ','204 North Border St.Pelham, AL 35124 ','vivaciousTerrance84@bigpond.net.au ','(577) 594-6796 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Dr. Jose Jewess ','7639 Oak CourtBluffton, SC 29910 ','crazyBrandi@hotmail.fr ','(465) 648-3305 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Lester Kilback ','849 Hill Field St.Lewis Center, OH 43035 ','hilariousBrian@home.nl ','(214) 569-0493 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Michel Greenholt IV ','716 Smith Store Ave.Champaign, IL 61821 ','elatedTrevor29@web.de ','(271) 302-3464 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Darrell Schiller V ','849 Hill Field St.Lewis Center, OH 43035 ','frailEmily92@yahoo.com.mx ','(468) 385-7059 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Mrs. Lera Morar ','716 Smith Store Ave.Champaign, IL 61821 ','Krystalperfect@aliceadsl.fr ','(713) 554-8658 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Alverta Nienow Sr. ','31 Rockaway Dr.Hamden, CT 06514 ','doubtfulHeather@t-online.de ','(448) 916-2060 ')
masseuseManager.insert_masseuse(random.randint(10000, 99999),'Jed Bernier III ','649 Indian Spring Ave.Elizabeth, NJ 07202 ','Gloriablue@mac.com ','(979) 258-7939 ')


availabilityManager.insert_availability(13741,2,9,16 )
availabilityManager.insert_availability(16056,2,9,16 )
availabilityManager.insert_availability(18791,2,9,16 )
availabilityManager.insert_availability(34734,2,9,16 )
availabilityManager.insert_availability(54253,2,9,16 )
availabilityManager.insert_availability(56089,2,9,16 )
availabilityManager.insert_availability(61333,2,9,16 )
availabilityManager.insert_availability(61789,2,9,16 )
availabilityManager.insert_availability(64724,2,9,16 )
availabilityManager.insert_availability(66549,2,9,16 )
availabilityManager.insert_availability(77843,2,9,16 )
availabilityManager.insert_availability(89062,2,9,16 )
availabilityManager.insert_availability(92744,2,9,16 )
availabilityManager.insert_availability(92960,2,9,16 )
availabilityManager.insert_availability(98543,2,9,16 )
availabilityManager.insert_availability(13741,3,9,16 )
availabilityManager.insert_availability(16056,3,9,16 )
availabilityManager.insert_availability(18791,3,9,16 )
availabilityManager.insert_availability(34734,3,9,16 )
availabilityManager.insert_availability(54253,3,9,16 )
availabilityManager.insert_availability(56089,3,9,16 )
availabilityManager.insert_availability(61333,3,9,16 )
availabilityManager.insert_availability(61789,3,9,16 )
availabilityManager.insert_availability(64724,3,9,16 )
availabilityManager.insert_availability(66549,3,9,16 )
availabilityManager.insert_availability(77843,3,9,16 )
availabilityManager.insert_availability(89062,3,9,16 )
availabilityManager.insert_availability(92744,3,9,16 )
availabilityManager.insert_availability(92960,3,9,16 )
availabilityManager.insert_availability(98543,3,9,16 )
availabilityManager.insert_availability(13741,4,9,16 )
availabilityManager.insert_availability(16056,4,9,16 )
availabilityManager.insert_availability(18791,4,9,16 )
availabilityManager.insert_availability(34734,4,9,16 )
availabilityManager.insert_availability(54253,4,9,16 )
availabilityManager.insert_availability(56089,4,9,16 )
availabilityManager.insert_availability(61333,4,9,16 )
availabilityManager.insert_availability(61789,4,9,16 )
availabilityManager.insert_availability(64724,4,9,16 )
availabilityManager.insert_availability(66549,4,9,16 )
availabilityManager.insert_availability(77843,4,9,16 )
availabilityManager.insert_availability(89062,4,9,16 )
availabilityManager.insert_availability(92744,4,9,16 )
availabilityManager.insert_availability(92960,4,9,16 )
availabilityManager.insert_availability(98543,4,9,16 )
availabilityManager.insert_availability(13741,5,9,16 )
availabilityManager.insert_availability(16056,5,9,16 )
availabilityManager.insert_availability(18791,5,9,16 )
availabilityManager.insert_availability(34734,5,9,16 )
availabilityManager.insert_availability(54253,5,9,16 )
availabilityManager.insert_availability(56089,5,9,16 )
availabilityManager.insert_availability(61333,5,9,16 )
availabilityManager.insert_availability(61789,5,9,16 )
availabilityManager.insert_availability(64724,5,9,16 )
availabilityManager.insert_availability(66549,5,9,16 )
availabilityManager.insert_availability(77843,5,9,16 )
availabilityManager.insert_availability(89062,5,9,16 )
availabilityManager.insert_availability(92744,5,9,16 )
availabilityManager.insert_availability(92960,5,9,16 )
availabilityManager.insert_availability(98543,5,9,16 )
availabilityManager.insert_availability(13741,6,9,16 )
availabilityManager.insert_availability(16056,6,9,16 )
availabilityManager.insert_availability(18791,6,9,16 )
availabilityManager.insert_availability(34734,6,9,16 )
availabilityManager.insert_availability(54253,6,9,16 )
availabilityManager.insert_availability(56089,6,9,16 )
availabilityManager.insert_availability(61333,6,9,16 )
availabilityManager.insert_availability(61789,6,9,16 )
availabilityManager.insert_availability(64724,6,9,16 )
availabilityManager.insert_availability(66549,6,9,16 )
availabilityManager.insert_availability(77843,6,9,16 )
availabilityManager.insert_availability(89062,6,9,16 )
availabilityManager.insert_availability(92744,6,9,16 )
availabilityManager.insert_availability(92960,6,9,16 )
availabilityManager.insert_availability(98543,6,9,16 )


"""
