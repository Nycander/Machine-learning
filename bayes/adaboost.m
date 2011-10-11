function [ mu, sigma, p, alpha, classes ] = adaboost( data, T )

w = [];
alpha = [];
mu = [];
sigma = [];
p = [];
classes = [];

w(1,:) = ones(size(data, 1), 1) ./ size(data, 1);
for t = 1:T
	[mu(t,:,:), sigma(t,:,:)] = bayes_weight(data, w(t,:));
	p(t,:) = prior(data, w(t,:))
	h = discriminant(data(:, 1:2), squeeze(mu(t,:,:)), squeeze(sigma(t,:,:)), p(t,:));

	ssum = 0;
	for m = 1:size(data)
		data(m,1:2)
		if h(data(m,1:2)) == data(m,3)
			ans = 0;
		else
			ans = 1;
		end
		ssum = ssum + w(t, m)*ans;
	end
	err = 1 - ssum;
	alpha(t) = log((1-err(t))/err(t))/2;
	for m = 1:size(data)
		w(t+1,m) = w(t,m);
		if h(data(m))==data(m,3)
			w(t+1,m) = w(t+1,m) * exp(-alpha(t));
		else
			w(t+1,m) = w(t+1,m) * exp(alpha(t));
		end
	end
	w(t+1,:) = w(t+1,:)/norm(w(t+1,:))
end
classes = unique(data(:,3))
