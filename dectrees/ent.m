
% Assumes data has 6 attributes, and the 7th column contains the classification

function entropy = ent(data)

p1 = sum(data(:,7))/size(data, 1);
p0 = 1 - p1;

entropy = -p0*log2(p0) - p1*log2(p1);

% From the book, page 56, "Notice that the entropy is 0 if all members of S belong to the same class"
if p1 == 1 || p0 == 1
	entropy = 0;
end