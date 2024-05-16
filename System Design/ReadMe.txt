Points to Remember:


1. CAP 
2. Load Balancing
3. Rate Limiting for Booking type of Design Makes the System Cost Effective and to Avoid Cascading Failure

	ALGORITHMS:
	1. TOKEN BUCKET  : 5 TOKENS / REQUESTS IN A MINUTE
	2. LEAKY BUCKET  : ADD REQUESTS TO QUEUE MAPPED TO SERVICE IF REQUEST SIZE IS TOO BIG TOO MANY REQUEST WILL BE REJECTED.
	3. FIXED WINDOW  : FOR 0-5 MINS ONLY 2 REQUESTS 5-10 2 REQUESTS AND SO ON
	4. SLIDING WINDOW : FOR A WINDOW SIZE ALLOW 5 REQUESTS ONLY 

4. CHOOSE OPTIMAL DATABASE SYSTEM : RDBMS OR NoSql DATABASE
5. DISTRIBUTED CACHE :
	uses : Imporves performance, reduce db load, inceares IOPS
	LRU (Doubly linked list most recent at end of list and remove from head)
	LFU (Map + Heap): on basis of frequency
6. Break The design into functional and non functional requirements:
	1. FUNCTIONAL REQUIREMENTS : Services you need to implement
	2. Non - Functional Requirements: Highly Available, low latency (nearly real time), validation of data 
