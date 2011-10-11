function [ mu, sigma ] = bayes( data )
	% Computes the maximum posterior (MAP) parameters mu and sigma for a given dataset

	% Compute mu
	for i=1:2 % Loop for every classification
		data_c = subset(data, 3, i-1);
		for n=1:2
			mu(i,n) = mean(data_c(:,n));
		end
	end

	% Compute sigma
	for i=1:2 % Loop for every classification
		data_c = subset(data, 3, i-1);
		for n=1:2
			sigma(i,n) = std(data_c(:,n));
		end
	end
end


