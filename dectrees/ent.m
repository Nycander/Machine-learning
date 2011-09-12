
% Assumes data has 6 attributes, and the 7th column contains the classification

function entropy = ent(data)

p1 = sum(data(:,7))/size(data, 1);
p0 = 1 - p1;

entropy = -p0*log2(p0) - p1*log2(p1);