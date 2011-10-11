function [ mu, sigma ] = bayes_weight( data, w )
	% Computes the maximum posterior (MAP) parameters mu and sigma for a given dataset
	% Compute mu
	for i=1:2 % Loop for every classification
		data_c = subset(data, 3, i-1);
		for n=1:2
			ssum = 0;
            wsum = 0;
			for m=1:size(data_c, 1)
				ssum = ssum + w(m) * data_c(m,n);
                wsum = wsum + w(m);
			end
			ssum = ssum / wsum;
			mu(i,n) = ssum;
		end
	end

	% Compute sigma
	for i=1:2 % Loop for every classification
		data_c = subset(data, 3, i-1);
		for n=1:2
			tmp_sum = 0;
            wsum = 0;
			for m = 1:size(data_c,1)
				tmp_sum = tmp_sum + w(m)*(data_c(m,n) - mu(i,n))^2;
                wsum = wsum + w(m);
			end
			sigma(i,n) = sqrt(tmp_sum / wsum);
		end
    end
    
end

