clc; clear;
%% Import data
cd 'data'
all_data_name = {'a_lvr_land_a','b_lvr_land_a','e_lvr_land_a',...
                 'f_lvr_land_a','h_lvr_land_a'};

s = length(all_data_name); data = cell(s,1);
for k = 1 : s
    tmp = append(all_data_name{k},'.csv');
    data{k} = readtable(tmp,'Format','auto');
end

%% Merge data
all_data = data{1}(2:end,:);
for k = 2 : s
    all_data = [all_data; data{k}(2:end,:)];
end
writetable(all_data,'All_data.xlsx');

cd ../

%%
