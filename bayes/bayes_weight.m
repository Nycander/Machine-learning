function [ mu, sigma ] = bayes_weight( data, w )
	% Computes the maximum posterior (MAP) parameters mu and sigma for a given dataset

	% Compute mu
	for i=1:2 % Loop for every classification
		data_c = subset(data, 3, i-1);
		for n=1:2
			for m=1:size(data_c, 1);
				ssum = ssum + w(m) * data_c(m,n);
			end
			ssum = ssum / sum(w);
			mu(i,n) = ssum;
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


