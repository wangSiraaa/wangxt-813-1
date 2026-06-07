INSERT INTO tree_archive (tree_code, species, location, street, category, age, diameter, health_status, plant_date, maintenance_unit) VALUES
('TR001', '悬铃木', '中山路1号', '中山路', 'ORDINARY', 15, 35.5, '良好', '2009-03-15', '城维养护公司'),
('TR002', '香樟', '中山路2号', '中山路', 'ORDINARY', 12, 28.0, '良好', '2012-04-20', '城维养护公司'),
('TR003', '国槐', '人民路1号', '人民路', 'ANCIENT_AND_FAMOUS', 120, 85.0, '健康', '1905-06-10', '古树名木保护中心'),
('TR004', '银杏', '人民路2号', '人民路', 'ANCIENT_AND_FAMOUS', 300, 120.0, '优良', '1726-08-15', '古树名木保护中心'),
('TR005', '杨树', '建设路1号', '建设路', 'ORDINARY', 8, 20.0, '一般', '2016-05-01', '绿源绿化公司');

INSERT INTO construction_section (section_name, location, occupy_start_date, occupy_end_date, current_application_no, is_occupied) VALUES
('中山路-东段', '中山路从东一环到东二环', NULL, NULL, NULL, FALSE),
('人民路-北段', '人民路从北一环到北二环', NULL, NULL, NULL, FALSE),
('建设路-中段', '建设路中间段', NULL, NULL, NULL, FALSE);
