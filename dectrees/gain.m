function [G] = gain(S)
	G = [];
	for attr = 1:6
		G(attr) = gainAttr(S, attr);
	end

function G = gainAttr(S, A)
	G = ent(S);
	Scount = size(S, 1);

	for k = values(S, A)'
		Sk = subset(S, A, k);
		G = G - (size(Sk, 1) / Scount) * ent(Sk);
	end