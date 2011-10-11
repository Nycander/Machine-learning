function c = adaboost_discriminant(data, mu, sigma, p, alpha, classes, T)

M = size(data, 1);
C = size(sigma, 1);

tempC = zeros(M, C);

for t = 1:T
	h = discriminant(data, mu(:,:,t), sigma(:,:,t), p(t,:));
	[dummy class] = max(h, [], 2);
	class = class -1;

	for c=1:C
		tempC(:,c) = tempC(:,c) + alpha(t)*(class==classes(c));
	end
end

[dummy c] = max(tempC, [], 2);
c = c-1;

