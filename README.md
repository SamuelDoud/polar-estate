# polar-estate
Maps locations of interest on a map by their polar coordinates with a user passed value as the origin. Will coupled together with other locations in a set it provides suggestions on the best origin locations given the user's preferences.



#####
Utiity Estimation
	In economics 'utility' is defined as "the total satisfaction received from consuming a good or service." Thus given a set of comprable buisnesses, the one we reccomend should be the one with the highest utility. However, the question of how to calculate this utility is complex. 

	Q: What factors should go into the utility of a particular business?
	1) distance. Everything held equal, people probably want to go to a closer store.
	2) quality. Everything held equal, people probably want better quality

	Q: How does utility vary by distance:
		the relationship between utility and distance can vary depending on the type of transport. For instance, users with cars are probably more willing to go further than someone who has to walk. However, no matter how far away something is, its never worth 0, as it still exists. Therefore, we think that utility is bounded by 0 as distance goes to infinity. Thus, we think a decent model is exponential decay. 

	FAQ 1: Can the utility of different kinds of buisnesses be calculated in the same way?
		Not neccessarily. People are more likley to drive far for a hospital than for a grocery store. 
		Also, in assessing the total quality of a location, there is diminishing marginal utility to each of type of buisness. 

	Q: How do we calculate utility overall?
		-Within each category, we calculate utility u(i) for each buisness i=1,2,3,4,.
		-We then sort these utilities, giving the highest u(i) index 1, and subsequent 2,3,4,.....
		-we multiply each of the sorted u(i) by a function representing diminishing marginal utility.
		-We then sum over these results. 
