function [err] = ass4(data, test)
for frac = (3:8)/10
    [n,m]=size(data);
    p=randperm(n);
    data_new=data(p(1:floor(n*frac)),:);
    data=data(p(floor(n*frac)+1:n),:);
    T1=build_tree(data_new);
    T1p=prune_tree(T1,data);
    err= [err calculate_error(T1p, test)];
end
