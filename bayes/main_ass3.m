hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
data1 = normalize_and_label(hand, 0);
data2 = normalize_and_label(book, 1);

test_data = [data2 ; data1];


adaboost(test_data, 6)
