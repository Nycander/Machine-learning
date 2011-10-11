function [ mu, sigma, p, alpha, classes ] = adaboost( data, T )

w = [];
alpha = [];
mu = [];
sigma = [];
p = [];
classes = unique(data(:,3));

w = ones(size(data, 1), 1) ./ size(data, 1);
for t = 1:T
	[mu(:,:,t), sigma(:,:,t)] = bayes_weight(data, w);
	p(t,:) = prior(data, w);

	h = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(t, :));
	[dummy class] = max(h, [], 2);
	class = class -1;

	err = 1 - sum(w.*(class == data(:,end)))
	alpha(t) = 0.5 * log((1-err)/err);
	alph = (data(:,end) == class)*-1;
	w = w.*exp(alph.*alpha(t));
	w = w./sum(w);
end
