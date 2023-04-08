## Filter by -
1. Properties
2. city
3. status
4. platform
5. month
6. week
7. weekend and weekday - In hotel industry weekend is Fri and Sat.

## Key Metrics -
1. ***revenue***
	1. **NetRevenue** = `SUM(FactBooking[revenue_realized])`
	2. **GrossRevenue** = `SUM(FactBooking[revenue_generated])`
2.  ***Bookings***
		1. **TotalBookings** = `CALCULATE(COUNTROWS(DISTINCT(FactBooking[booking_id])))`
		2. **TotalSuccessfulBooking** = `SUM(FactAggregatedBooking[successful_bookings])`
		3. **TotalCancelledBookings** = `CALCULATE([TotalBooking],FILTER(FactBooking,[booking_status] = "Cancelled"))`
		4. **Booking %** = `DIVIDE([TotalBooking],CALCULATE([TotalBooking],REMOVEFILTERS(FactBooking[booking_status])))`
		5. **Cancelled %** = `CALCULATE([booking %],FactBooking[booking_status]="Cancelled")`
		6. **Checked Out %** = `CALCULATE([booking %],FactBooking[booking_status]="Checked Out")`
		7. It is also known as **Realization %**
		8. **No Show %** = `CALCULATE([booking %],FactBooking[booking_status]="No Show")`
		9. **Booking % by room class** : To show the percentage contribution of each room class over total rooms booked. We have room classes like Standard, Elite, Premium, Presidential.
			1. `booking % By room_class = DIVIDE([TotalBooking],CALCULATE([TotalBooking],ALL(DimRooms[room_class])))`
		10. **Booking % by channel** : To show the percentage contribution of each booking platform for bookings in hotels. We have booking platforms like makeyourtrip, logtrip, tripster etc)
			1. `booking % ByChannel = DIVIDE([TotalBooking],CALCULATE([TotalBooking],ALL(FactBooking[booking_platform])))`
3. ***available rooms***
		1. **AvailableRooms** = `sum(FactAggregatedBooking[capacity])`
		2. the available rooms are in hotel industry were called `SRN`
		3. **SRN**  is sellable room nights
			1. as it calculated on daily basis it is called as `DSRN`
		4. **DSRN** -  Daily sellable rooms per night.
			1. This metrics tells, on average how many rooms are ready to sell for a day considering a time period
			2. `DSRN = DIVIDE([SRN],[TotalDay])`
		5. **DBRN** - Daily booked room per night
			1. This metrics tells on average how many rooms are booked for a day considering a time period
			2. `DBRN = [BookedRooms]/[TotalDays]`
		6. **DURN** -  Daily utilized room per night
			1. This metric tells on average how many rooms are successfully utilized by customers for a day considering a time period.
			2. `DURN = DIVIDE([CheckedOutCount],[TotalDays])`
4. ***occupancy*** - total room occupied / total room available
		1. you have 100 room hotel. on Monday 50 customers were checked out so occupancy for Sunday would be 50
		2. `occupancy % = DIVIDE([SuccessfulBookings],[AvailableRooms])`
5. ***avg rating***
		1. `AverageRatings = AVERAGE(FactBooking[ratings_given])`
6. ***Workduration*** 
		1. `TotalDay = DATEDIFF(MIN(FactBooking[check_in_date]),MAX(FactBooking[check_in_date]),DAY) +1`
	- 
7. ***REVPAR*** - revenue per available rooms (total revenue/total available rooms) or ADR * OCCUPANCY
		1. If you have 100 room hotel and 5 are out of order. then accual available room count is now 95. so if you sold 50 rooms then occupancy rate will be 50/95 not 50/100.
		2. revpar will be total revenue generate by 50 rooms  divided by 95.
		3. so available rooms are vey important key metric.
8. ***ADR***  - average daily rate 
		1. `DIVIDE([NetRevenue],[SuccessfulBookings],0)`
		2. total revenue /  number of room you sold
		3. If you sold 50 rooms and each room were sold in 1000 rupees you ADR will be 1000.
		4. If you occupancy is 100% your ADR and REVPAR will be equal.
---
## Level One analysis
1. ***Realisation*** - `URN` / `BRN`
		1. **URN** - utilized room nights -  In 100 rooms hotel and 100 are available rooms if on sunday 50 rooms are booked and customer stayed then `URN` will be 50. when customer staying in room that room is under urn.
		2. **BRN** - Booked room nights - In 100 rooms hotel and 100 rooms are available. if on sunday 60 rooms are booked and only 50 customers are stayed. then `BRN` will be 60 and `URN` will be 50. 
		3. `BRN` = `URN` + `CANCLLED`+`NO SHOW`
		4. **NO SHOW** -  booked and no cancellation and not stayed 
		5. **Revenue WoW change %** : To get the revenue change percentage week over week.
