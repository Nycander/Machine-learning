function [ g ] = discriminant( data, mu, sigma, p )

	g = [];
	for i=1:2 % Loop over all classifications

		ssum1 = 0;
		ssum2 = 0;
		for n=1:2
			ssum1 = ssum1 + log(sigma(i,n));
			ssum2 = ssum2 + (data(:, n) - mu(i,n)).^2 / (2*(sigma(i,n).^2));
		end

		g(i,:) = log(p(i)) - ssum1 - ssum2 ;
	end
	g = transpose(g);
end

