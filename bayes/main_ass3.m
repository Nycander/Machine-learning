
hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);

test_data = [data2 ; data1];

w = ones(size(test_data, 1), 1) ./ size(test_data, 1);

[mu, sigma] = bayes_weight(test_data, w)
