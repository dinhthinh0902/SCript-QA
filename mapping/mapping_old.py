##------------------------------------------------------
## SAY SOME THING
##------------------------------------------------------

DIM_NhomDichVu = [ #1
	#TargetField			SourceField		ReferenceTable					ForeignKey		MapField
	('NhomDichVu_Key',		None,				 None,						None,			None),
	('NhomDichVu_Id',		'NhomDichVu_Id',	 None,						None,			None),
	('MaNhomDichVu',		'MaNhomDichVu',		 None,						None,			None),
	('LoaiDichVu_Id',		'LoaiDichVu_Id',	 None,						None,			None),
	('TenNhomDichVu',		'TenNhomDichVu',	 None,						None,			None),
	('TenNhomDichVu_En',	'TenNhomDichVu_En',	 None,						None,			None),
	('TenNhomDichVu_Ru',	'TenNhomDichVu_Ru',	 None,						None,			None),
	('Cap',					'Cap',				 None,						None,			None),
	# ('CapTren_Key',			'CapTren_Id',		 'DIM_NhomDichVu',		'NhomDichVu_Key',	None),
	('TraLoiKetQuaRieng',	'TraLoiKetQuaRieng', None,						None,			None),
	('TamNgung',			'TamNgung',			 None,						None,			None),
	('TenKhongDau',			'TenKhongDau',		 None,						None,			None),
	('NgayTao_Key',			'NgayTao',			 'DIM_Date',				'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		 None,						None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',		 'DIM_Date',				'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	 None,						None,			None),
	('PrefixCode',			'PrefixCode',		 None,						None,			None)
	#('Source_Key',			None,				 'DIM_BenhVien',			'BenhVien_Key', None)
]

DIM_DichVu = [ #2
	#TargetField					SourceField						ReferenceTable		ForeignKey		MapField
	('DichVu_Key',					None,								None,			None,			None),
	('DichVu_Id',					'DichVu_Id',						None,			None,			None),
	('NhomDichVu_Id',				'NhomDichVu_Id',				'DIM_NhomDichVu',	'NhomDichVu_Key',	'NhomDichVu_Id'),
	('MaDichVu',					'MaDichVu',							None,			None,			None),
	('MaDichVu_Seg01',				'MaDichVu_Seg01',					None,			None,			None),
	('MaDichVu_Seg02',				'MaDichVu_Seg02',					None,			None,			None),
	('MaDichVu_Seg03',				'MaDichVu_Seg03',					None,			None,			None),
	('MaDichVu_Seg04',				'MaDichVu_Seg04',					None,			None,			None),
	('TenDichVu',					'TenDichVu',						None,			None,			None),
	('TenDichVu_En',				'TenDichVu_En',						None,			None,			None),
	('TenDichVu_Ru',				'TenDichVu_Ru',						None,			None,			None),
	# ('Cap',							'Cap',							'Cap',			None,			None),
	# ('CapTren_Key',					'CapTren_Id',					'DIM_DichVu',	'DIM_DichVu_Key',	None),
	('DonViTinh',					'DonViTinh',						None,			None,			None),
	('Idx',							'Idx',								None,			None,			None),
	('ChonHetCapDuoi',				'ChonHetCapDuoi',					None,			None,			None),
	('CoGiaDichVu',					'CoGiaDichVu',						None,			None,			None),
	('GiaCoDinh',					'GiaCoDinh',						None,			None,			None),
	('ThucHienBenNgoai',			'ThucHienBenNgoai',					None,			None,			None),
	('SoPhim',						'SoPhim',							None,			None,			None),
	('MaQuiDinh',					'MaQuiDinh',						None,			None,			None),
	('TamNgung',					'TamNgung',							None,			None,			None),
	('TenKhongDau',					'TenKhongDau',						None,			None,			None),
	('NgayTao_Key',					'NgayTao',							'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiTao_Id',					'NguoiTao_Id',						None,			None,			None),
	('NgayCapNhat_Key',				'NgayCapNhat',						'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',				'NguoiCapNhat_Id',					None,			None,			None),
	('CoGiaTriChuan',				'CoGiaTriChuan',					None,			None,			None),
	('Test',						'Test',								None,			None,			None),
	('Attribute1',					'Attribute1',						None,			None,			None),
	('Attribute2',					'Attribute2',						None,			None,			None),
	('Attribute3',					'Attribute3',						None,			None,			None),
	('Attribute4',					'Attribute4',						None,			None,			None),
	('Attribute5',					'Attribute5',						None,			None,			None),
	('NhomDichVu_Report_Local_Id',	'NhomDichVu_Report_Local_Id',		None,			None,			None),
	('NhomDichVu_Report_Global_Id',	'NhomDichVu_Report_Global_Id',		None,			None,			None),
	('ShortName',					'ShortName',						None,			None,			None),
	('InputCode',					'InputCode',						None,			None,			None),
	('NoResult',					'NoResult',							None,			None,			None),
	('ApplyFor',					'ApplyFor',							None,			None,			None),
	('PrintWhenNull',				'PrintWhenNull',					None,			None,			None),
	('ReportCode',					'ReportCode',						None,			None,			None),
	('ReportTitle',					'ReportTitle',						None,			None,			None),
	('DoUuTienDichVu',				'DoUuTienDichVu',					None,			None,			None),
	('MaMay',						'MaMay',							None,			None,			None),
	('BHYT',						'BHYT',								None,			None,			None),
	('DacDiemDacBiet',				'DacDiemDacBiet',					None,			None,			None),
	('HideGroup',					'HideGroup',						None,			None,			None),
	('LoaiBenhPham_Id',				'LoaiBenhPham_Id',					None,			None,			None),
	('STTDV',						'STTDV',							None,			None,			None)
	# ('Source_Key',					'BenhVien_Key',						None,			None,			None)
]				

DIM_DonViTinh = [ #3
	#TargetField			SourceField		ReferenceTable		ForeignKey		MapField
	('DonViTinh_Key',		None,				None,			None,			None),
	('DonViTinh_Id',		'DonViTinh_Id',		None,			None,			None),
	('LoaiVatTu_Key',		'LoaiVatTu_Id',		'DIM_LoaiVatTu','LoaiVatTu_Key', 'LoaiVatTu_Key'),
	('MaDonViTinh',			'MaDonViTinh',		None,			None,			None),
	('TenDonViTinh',		'TenDonViTinh',		None,			None,			None),
	('DonViCoBan',			'DonViCoBan',		None,			None,			None),
	('DonViCoBan_Id',		'DonViCoBan_Id',	None,			None,			None),
	('GiaTriQuiDoi',		'GiaTriQuiDoi',		None,			None,			None),
	('TenKhongDau',			'TenKhongDau',		None,			None,			None),
	('TamNgung',			'TamNgung',			None,			None,			None),
	('NgayTao_Key',			'NgayTao',			'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		None,			None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',		'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,			None,			None),
	('TenDonViTinh_En',		'TenDonViTinh_En',	None,			None,			None)
]

DIM_LoaiVatTu = [ #4
	#TargetField			SourceField		ReferenceTable		ForeignKey		MapField
	('LoaiVatTu_Keya',		None,				None,			None,			None),
	('LoaiVatTu_Key',		'LoaiVatTu_Id',		None,			None,			None),
	('TenLoaiVatTu',		'TenLoaiVatTu',		None,			None,			None),
	('TenLoaiVatTu_En',		'TenLoaiVatTu_En',	None,			None,			None),
	('TenLoaiVatTu_Ru',		'TenLoaiVatTu_Ru',	None,			None,			None),
	('TamNgung',			'TamNgung',			None,			None,			None),
	('TenKhongDau',			'TenKhongDau',		None,			None,			None),
	('NgayTao_Key',			'NgayTao',			'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		None,			None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',		'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,			None,			None),
	('TinhVATVaoGiaVon',	'TinhVATVaoGiaVon',	None,			None,			None),
	('TKHangTonKho',		'TKHangTonKho',		None,			None,			None),
	('TKChiPhi',			'TKChiPhi',			None,			None,			None)
	#('Source_Key',			'BenhVien_Key',		None,			None,			None)
]

DIM_ICD = [ #5
	#TargetField			SourceField		ReferenceTable		ForeignKey		MapField
	('ICD_Key',				None,				None,			None,			None),
	('ICD_Id',				'ICD_Id',			None,			None,			None),
	('MaICD',				'MaICD',			None,			None,			None),
	('TenICD',				'TenICD',			None,			None,			None),
	('TenICD_En',			'TenICD_En',		None,			None,			None),
	('TenICD_Ru',			'TenICD_Ru',		None,			None,			None),
	('MucICD',				'MucICD',			None,			None,			None),
	('ICD_Nhom_Id',			'ICD_Nhom_Id',		None,			None,			None),
	('PhanNhom',			'PhanNhom',			None,			None,			None),
	('Loai',				'Loai',				None,			None,			None),
	('BenhTruyenNhiem',		'BenhTruyenNhiem',	None,			None,			None),
	('TamNgung',			'TamNgung',			None,			None,			None),
	('TenKhongDau',			'TenKhongDau',		None,			None,			None),
	('NgayTao_Key',			'NgayTao',			'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		None,			None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',		'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,			None,			None),
	('Ma',					'Ma'			,	None,			None,			None),
	('ChanDoanHinhAnh',		'ChanDoanHinhAnh',	None,			None,			None)
	#('Source_Key',			'BenhVien_Key',		None,			None,			None)
]

DIM_Duoc = [ #6
	#TargetField			SourceField			ReferenceTable		ForeignKey		MapField
	('Duoc_Key',			None,				None,				None,			None),
	('Duoc_Id',				'Duoc_Id',			None,				None,			None),
	('MaDuoc',				'MaDuoc',			None,				None,			None),
	('TenDuoc_Id',			'TenDuoc_Id',		None,				None,			None),
	('DonViTinh_Key',		'DonViTinh_Id',		'DIM_DonViTinh',	'DonViTinh_Key',	'DonViTinh_Id'),
	('HamLuong',			'HamLuong',			None,				None,			None),
	('QuocGia_Key',			'QuocGia_Id',		'DIM_QuocGia',		'QuocGia_Key',	'QuocGia_Id'),
	('HangSanXuat_Key',		'HangSanXuat_Id',	None,				None,			None),
	('LoaiDuoc_Key',		'LoaiDuoc_Id',		'DIM_LoaiDuoc',		'LoaiDuoc_Key',	'LoaiDuoc_Id'),
	('PhanNhomDuoc_Key',	'PhanNhomDuoc_Id',	'DIM_PhanNhomDuoc',	'PhanNhomDuoc_Key',	'PhanNhomDuoc_Id'),
	('PhanLoaiDuoc',		'PhanLoaiDuoc',		None,				None,			None),
	# ('DuongDung_Code',		'DuongDung_Id',		'Lst_Dictionary',	'Dictionary_Code',	'Dictionary_Type_Code'),
	# ('DuongDung_Name',		None,				'Lst_Dictionary',	'Dictionary_Name',	None),
	# ('DuongDung_Name_En',	None,				'Lst_Dictionary',	'Dictionary_Name_En', None),
	('BHYT',				'BHYT',				None,				None,			None),
	('QuanTamDacBiet',		'QuanTamDacBiet',	None,				None,			None),
	('CongDung',			'CongDung',			None,				None,			None),
	('TamNgung',			'TamNgung',			None,				None,			None),
	('NgayTao_Key',			'NgayTao',			None,				None,			None),
	('NguoiTao_Id',			'NguoiTao_Id',		None,				None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',		None,				None,			None),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,				None,			None),
	('MaKeToan',			'MaKeToan',			None,				None,			None),
	('SoTaiKhoan',			'SoTaiKhoan',		None,				None,			None),
	('SoThamChieu',			'SoThamChieu',		None,				None,			None),
	('TamNgungDuTru',		'TamNgungDuTru',	None,				None,			None),
	('TenHang',				'TenHang',			None,				None,			None),
	('DonViTinh',			'DonViTinh',		None,				None,			None),
	('HangSanXuat',			'HangSanXuat',		None,				None,			None),
	('QuocGia',				'QuocGia',			None,				None,			None),
	('TenDuocDayDu',		'TenDuocDayDu',		None,				None,			None),
	('AutoCompleteField',	'AutoCompleteField',None,				None,			None),
	('TenHoatChat',			'TenHoatChat',		None,				None,			None),
	('PhamVi',				'PhamVi',			None,				None,			None),
	('HoatChat_Key',		'HoatChat_Id',		None,				None,			None),
	('MaDuoc_1',			'MaDuoc_1',			None,				None,			None),
	('MaDuoc_2',			'MaDuoc_2',			None,				None,			None),
	('CachSuDung',			'CachSuDung',		None,				None,			None),
	('HamLuongChiTiet',		'HamLuongChiTiet',	None,				None,			None),
	('KhoQuanLy_Id',		'KhoQuanLy_Id',		None,				None,			None),
	('Attribute_1',			'Attribute_1',		None,				None,			None),
	('Attribute_2',			'Attribute_2',		None,				None,			None),
	('Attribute_3',			'Attribute_3',		None,				None,			None),
	('Attribute_4',			'Attribute_4',		None,				None,			None),
	('HangKyGoi',			'HangKyGoi',		None,				None,			None),
	('TinhTien',			'TinhTien',			None,				None,			None),
	('Subgroup',			'Subgroup',			None,				None,			None),
	('Sub_subgroup',		'Sub_subgroup',		None,				None,			None),
	('MaDuocCIH',			'MaDuocCIH',		None,				None,			None),
	('TacDungPhu',			'TacDungPhu',		None,				None,			None),
	('MaDuocCIH_So',		'MaDuocCIH_So',		None,				None,			None),
	('DonViDung_Id',		'DonViDung_Id',		None,				None,			None),
	('TenBV',				'TenBV',			None,				None,			None),
	('QLLo',				'QLLo',				None,				None,			None),
	('Brandname',			'Brandname',		None,				None,			None),
	('KeDon',				'KeDon',			None,				None,			None),
	('ATC',					'ATC',				None,				None,			None),
	('PT_BNTraTien',		'PT_BNTraTien',		None,				None,			None),
	('Ven_Id',				'Ven_Id',			None,				None,			None),
	('STTD',				'STTD',				None,				None,			None),
	('MaNhom',				'MaNhom',			None,				None,			None),
	('TenVTYT',				'TenVTYT',			None,				None,			None),
	('VTYTDanTem',			'VTYTDanTem',		None,				None,			None),
	('DinhMuc',				'DinhMuc',			None,				None,			None),
	('DangBaoChe',			'DangBaoChe',		None,				None,			None),
	('SoDangKy',			'SoDangKy',			None,				None,			None),
	('MaHoatChat',			'MaHoatChat',		None,				None,			None),
	('MaDuongDung',			'MaDuongDung',		None,				None,			None),
	('VAT',					'VAT',				None,				None,			None),
	('SoLuongDacBiet',		'SoLuongDacBiet',	None,				None,			None)
	# ('Source_Key',			'BenhVien_Key',		None,				None,			None)
]

DIM_PhanNhomDuoc = [ #7
	#TargetField			SourceField				ReferenceTable		ForeignKey			MapField
	('LoaiDuoc_Key',		None,					None,				None,				None),
	('PhanNhomDuoc_Id',		'PhanNhomDuoc_Id',		None,				None,				None),
	('MaPhanNhomDuoc',		'MaPhanNhomDuoc',		None,				None,				None),
	('TenPhanNhomDuoc',		'TenPhanNhomDuoc',		None,				None,				None),
	('TenPhanNhomDuoc_En',	'TenPhanNhomDuoc_En',	None,				None,				None),
	('TenPhanNhomDuoc_Ru',	'TenPhanNhomDuoc_Ru',	None,				None,				None),
	# ('NhomDuoc_Key',		'NhomDuoc_Id',			'DM_NhomDuoc',		'NhomDuoc_Id',		None),
	# ('MaNhomDuoc',			None,					'DM_NhomDuoc',		'MaNhomDuoc',		None),
	# ('TenNhomDuoc',			None,					'DM_NhomDuoc',		'TenNhomDuoc',		None),
	# ('TenNhomDuoc_En',		None,					'DM_NhomDuoc',		'TenNhomDuoc_En',	None),
	('TamNgung',			'TamNgung',				None,				None,				None),
	('TenKhongDau',			'TenKhongDau',			None,				None,				None),
	('NgayTao_Key',			'NgayTao',				'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',			None,				None,				None),
	('NgayCapNhat_Key',		'NgayCapNhat',			'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None,				None,				None)
	# ('Source_Key',			'BenhVien_Key',			None,				None,				None)
]

DIM_LoaiDuoc = [ #8
	#TargetField				SourceField				ReferenceTable		ForeignKey			MapField
	('LoaiDuoc_Key',			None,					None,				None,				None),
	('LoaiDuoc_Id',				'LoaiDuoc_Id',			None,				None,				None),
	('MaLoaiDuoc',				'MaLoaiDuoc',			None,				None,				None),
	('TenLoaiDuoc',				'TenLoaiDuoc',			None,				None,				None),
	('TenLoaiDuoc_En',			'TenLoaiDuoc_En',		None,				None,				None),
	('TenLoaiDuoc_Ru',			'TenLoaiDuoc_Ru',		None,				None,				None),
	('LoaiVatTu_Id',			'LoaiVatTu_Id',			None,				None,				None),
	('NhomLoaiDuoc_Key',		'NhomLoaiDuoc_Id',		None,				None,				None),
	('QuanLyHanSuDung',			'QuanLyHanSuDung',		None,				None,				None),
	('Idx',						'Idx',					None,				None,				None),
	('TamNgung',				'TamNgung',				None,				None,				None),
	('TenKhongDau',				'TenKhongDau',			None,				None,				None),
	('NgayTao',					'NgayTao',				'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiTao_Id',				'NguoiTao_Id',			None,				None,				None),
	('NgayCapNhat',				'NgayCapNhat',			'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',			'NguoiCapNhat_Id',		None,				None,				None),
	('TieuKhoanHangTonKho',		'TieuKhoanHangTonKho',	None,				None,				None),
	('TieuKhoanChiPhi',			'TieuKhoanChiPhi',		None,				None,				None)
	# ('Source_Key',				'BenhVien_Key',			None,				None,				None)
]

DIM_DonViHanhChinh = [ #9
	#TargetField				SourceField				ReferenceTable		ForeignKey			MapField
	('DonViHanhChinh_Key',		None,					None,				None,				None),
	('DonViHanhChinh_Id',		'DonViHanhChinh_Id',	None,				None,				None),
	('MaDonVi',					'MaDonVi',				None,				None,				None),
	('TenDonVi',				'TenDonVi',				None,				None,				None),
	('CapDonVi',				'CapDonVi',				None,				None,				None),
	('CapTren_Id',				'CapTren_Id',			None,				None,				None),
	('MaVung_Id',				'MaVung_Id',			None,				None,				None),
	('KhuVucLuuTru_Id',			'KhuVucLuuTru_Id',		None,				None,				None),
	('TamNgung',				'TamNgung',				None,				None,				None),
	('TenTat',					'TenTat',				None,				None,				None),
	('TenTat_2',				'TenTat_2',				None,				None,				None),
	('TenTat_3',				'TenTat_3',				None,				None,				None),
	('TenKhongDau',				'TenKhongDau',			None,				None,				None),
	('NgayTao_Key',				'NgayTao',				'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiTao_Id',				'NguoiTao_Id',			None,				None,				None),
	('NgayCapNhat_Key',			'NgayCapNhat',			'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',			'NguoiCapNhat_Id',		None,				None,				None)
	# ('Source_Key',				'BenhVien_Key',			None,				None,				None)
]

DIM_BenhNhan = [ #10
	#TargetField					SourceField					ReferenceTable			ForeignKey				MapField
	('BenhNhan_Key',				None,						None,					None,					None),
	('BenhNhan_Id',					'BenhNhan_Id',				None,					None,					None),
	('MaYTe',						'MaYTe',					None,					None,					None),
	('MaBenhVien',					'MaBenhVien',				None,					None,					None),
	('SoVaoVien',					'SoVaoVien',				None,					None,					None),
	('TenBenhNhan',					'TenBenhNhan',				None,					None,					None),
	('Ho',							'Ho',						None,					None,					None),
	('Ten',							'Ten',						None,					None,					None),
	('GioiTinh',					'GioiTinh',					None,					None,					None),
	('NgaySinh_Key',				'NgaySinh',					'DIM_Date',				'Date_Key',				'Ngay'),
	('NamSinh',						'NamSinh',					None,					None,					None),
	('SoNha',						'SoNha',					None,					None,					None),
	('DiaChi',						'DiaChi',					None,					None,					None),
	# ('NhomMau',						'NhomMau_Id',				'Lst_Dictionary',		'Dictionary_Id',		None),
	# ('YeuToRh',						'YeuToRh_Id',				'Lst_Dictionary',		'Dictionary_Id',		None),
	('TienSuDiUng',					'TienSuDiUng',				None,					None,					None),
	('SoLuuTruNgoaiTru',			'SoLuuTruNgoaiTru',			None,					None,					None),
	('SoLuuTruNoiTru',				'SoLuuTruNoiTru',			None,					None,					None),
	('QuocTich_Key',				'QuocTich_Id',				'DIM_QuocGia',			'QuocGia_Key',			'QuocTich_Id'),
	# ('DonViHanhChinh_Key',			'TinhThanh_Id QuanHuyen_Id XaPhuong_Id', 	'DIM_DonViHanhChinh',	'DonViHanhChinh_Key',	None),
	# ('DanToc_Key',					'DanToc_Id',			'DIM_DanToc',			'DanToc_Key',			None),
	# ('NgheNghiep_Key',				'NgheNghiep_Id',		'DIM_NgheNghiep',		'NgheNghiep_Key',		None),
	('VietKieu',					'VietKieu',					None,					None,					None),
	('NguoiNuocNgoai',				'NguoiNuocNgoai',			None,					None,					None),
	('CMND',						'CMND',						None,					None,					None),
	('HoChieu',						'HoChieu',					None,					None,					None),
	('TenKhongDau',					'TenKhongDau',				None,					None,					None),
	('GhiChu',						'GhiChu',					None,					None,					None),
	('NgayTao_Key',					'NgayTao',					'DIM_Date',				'Date_Key',				'Ngay'),
	('NguoiTao_Id',					'NguoiTao_Id',				None,					None,					None),
	('NgayCapNhat_Key',				'NgayCapNhat',				'DIM_Date',				'Date_Key',				'Ngay'),
	('NguoiCapNhat_Id',				'NguoiCapNhat_Id',			None,					None,					None),
	('NgayCapThe_Key',				'NgayCapThe',				'DIM_Date',				'Date_Key',				'Ngay'),
	('NamCapThe',					'NamCapThe',				None,					None,					None),
	# ('ThoiGianCapThe_Key',			'ThoiGianCapThe',			'DIM_Time',				'Time_Key',				None),
	('NhanVien_Key',				'NhanVien_Id',				'DIM_NhanVien',			'NhanVien_Key',			'NhanVien_Id'),
	('TienSuBenh',					'TienSuBenh',				None,					None,					None),
	('TienSuHutThuocLa',			'TienSuHutThuocLa',			None,					None,					None),
	('DonViCongTac_Id',				'DonViCongTac_Id',			None,					None,					None),
	('SoDienThoai',					'SoDienThoai',				None,					None,					None),
	('DiaChiThuongTru',				'DiaChiThuongTru',			None,					None,					None),
	('DiaChiLienLac',				'DiaChiLienLac',			None,					None,					None),
	('Email',						'Email',					None,					None,					None),
	('DiaChiCoQuan',				'DiaChiCoQuan',				None,					None,					None),
	('TuVong',						'TuVong',					None,					None,					None),
	('NgayTuVong_Key',				'NgayTuVong',				None,					None,					None),
	('ThoiGianTuVong',				'ThoiGianTuVong',			None,					None,					None),
	('NguyenNhanTuVong_Id',			'NguyenNhanTuVong_Id',		None,					None,					None),
	('NguoiGhiNhanTuVong_Id',		'NguoiGhiNhanTuVong_Id',	None,					None,					None),
	('ThoiGianGhiNhanTuVong_Key',	'ThoiGianGhiNhanTuVong',	None,					None,					None),
	('CountNotes',					'CountNotes',				None,					None,					None),
	('NgayTaoBenhNhan_Key',			'NgayTaoBenhNhan',			'DIM_Date',				'Date_Key',				'Ngay'),
	('TienCan',						'TienCan',					None,					None,					None),
	('BenhManTinh',					'BenhManTinh',				None,					None,					None),
	('BenhDiTruyen',				'BenhDiTruyen',				None,					None,					None),
	('ChiDinhDacBiet',				'ChiDinhDacBiet',			None,					None,					None),
	# ('MoiQuanHe',					'MoiQuanHe_Id',				'Lst_Dictionary',		'Dictionary_Id',		None),
	('DiaChi_NLH',					'DiaChi_NLH',				None,					None,					None),
	('DienThoai_NLH',				'DienThoai_NLH',			None,					None,					None),
	('NguoiLienHe_Id',				'NguoiLienHe_Id',			None,					None,					None),
	('NguoiLienHe',					'NguoiLienHe',				None,					None,					None),
	('TinhTrangHonNhan_Id',			'TinhTrangHonNhan_Id',		None,					None,					None),
	('DienThoaiBan',				'DienThoaiBan',				None,					None,					None),
	('NgayHetHan_Passport_Key',		'NgayHetHan_Passport',		'DIM_Date',				'Date_Key',				'Ngay'),
	('CTBH_1',						'CTBH_1',					None,					None,					None),
	('CTBH_2',						'CTBH_2',					None,					None,					None),
	('CTBH_3',						'CTBH_3',					None,					None,					None),
	('HoTruocTen',					'HoTruocTen',				None,					None,					None),
	('NgayCapCMND',					'NgayCapCMND',				None,					None,					None),
	('NoiCapCMND',					'NoiCapCMND',				None,					None,					None),
	('GoiPACS',						'GoiPACS',					None,					None,					None),
	('PIDPACS',						'PIDPACS',					None,					None,					None),
	('ThuocLa',						'ThuocLa',					None,					None,					None),
	('VanDong',						'VanDong',					None,					None,					None),
	('Ruou',						'Ruou',						None,					None,					None),
	('CaPhe',						'CaPhe',					None,					None,					None),
	('Tra',							'Tra',						None,					None,					None),
	('ThuocDangDung',				'ThuocDangDung',			None,					None,					None),
	('DCTamTru',					'DCTamTru',					None,					None,					None),
	('QuocGia_Key',					'QuocGia_Id',				'DIM_QuocGia',			'QuocGia_Key',			'QuocGia_Id'),
	('BenhNhanCu_Id',				'BenhNhanCu_Id',			None,					None,					None)
	# ('Source_Key',					None,						'DIM_BenhVien',			'BenhVien_Key',			None)
]

DIM_PhongBan = [ #11
	#TargetField				SourceField				ReferenceTable			ForeignKey				MapField
	('PhongBan_Key',			None,					None,					None,					None),
	('PhongBan_Id',				'PhongBan_Id',			None,					None,					None),
	('MaPhongBan',				'MaPhongBan',			None,					None,					None),
	('TenPhongBan',				'TenPhongBan',			None,					None,					None),
	('TenPhongBan_En',			'TenPhongBan_En',		None,					None,					None),
	('TenPhongBan_Ru',			'TenPhongBan_Ru',		None,					None,					None),
	# ('LoaiPhongBan_Id',			'LoaiPhongBan_Id',		'Lst_Dictionary',		'Dictionary_Id',		None),
	# ('LoaiPhongBan_Code',		None,					'Lst_Dictionary',		'Dictionary_Code',		None),
	# ('LoaiPhongBan_Name',		None,					'Lst_Dictionary',		'Dictionary_Name',		None),
	# ('LoaiPhongBan_Name_En',	None,					'Lst_Dictionary',		'Dictionary_Name_En',	None),
	('Cap',						'Cap',					None,					None,					None),
	# ('CapTren_Key',				'CapTren_Id',			'DIM_PhongBan',			'CapTren_Key',			None),
	('TruongPhong_Key',			'TruongPhong',			'DIM_NhanVien',			'NhanVien_Key',			None),
	# ('LoaiPhongBenh_Id',		'LoaiPhongBenh_Id',		'Lst_Dictionary',		'Dictionary_Id',		None),
	# ('LoaiPhongBenh_Code',		None,					'Lst_Dictionary',		'Dictionary_Code',		None),
	# ('LoaiPhongBenh_Name',		None,					'Lst_Dictionary',		'Dictionary_Name',		None),
	# ('LoaiPhongBenh_Name_En',	None,					'Lst_Dictionary',		'Dictionary_Name_En',	None),
	('TamNgung',				'TamNgung',				None,					None,					None),
	('TenKhongDau',				'TenKhongDau',			None,					None,					None),
	('NgayTao_Key',				'NgayTao',				'DIM_Date',				'Date_Key',				'Ngay'),
	('NguoiTao_Id',				'NguoiTao_Id',			None,					None,					None),
	('NgayCapNhat_Key',			'NgayCapNhat',			'DIM_Date',				'Date_Key',				'Ngay'),
	('NguoiCapNhat_Id',			'NguoiCapNhat_Id',		None,					None,					None),
	('CoThucHienDichVu',		'CoThucHienDichVu',		None,					None,					None),
	('Idx',						'Idx',					None,					None,					None),
	('QuanLyNhanSu',			'QuanLyNhanSu',			None,					None,					None),
	('IsKhoaDieuTri',			'IsKhoaDieuTri',		None,					None,					None),
	('IsChuyenKhoa',			'IsChuyenKhoa',			None,					None,					None),
	('CostCenTer_Id',			'CostCenTer_Id',		None,					None,					None),
	('ChuyenKhoa_Key',			'ChuyenKhoa_Id',		None,					None,					None),
	('Tang',					'Tang',					None,					None,					None)
	# ('Source_Key',				None,					'DIM_BenhVien',			'BenhVien_Key',			None)
]

DIM_GiuongBenh = [ #12
	#TargetField				SourceField				ReferenceTable			ForeignKey			MapField
	('GiuongBenh_Key',			None,					None,					None,				None),
	('GiuongBenh_Id',			'GiuongBenh_Id',		None,					None,				None),
	('MaGiuong',				'MaGiuong',				None,					None,				None),
	# ('KhoaDieuTri_Key',			'KhoaDieuTri_Id',		'DIM_PhongBan',			'PhongBan_Key',		None),
	('PhongBenh_Id',			'PhongBenh_Id',			None,					None,				None),
	('Tang',					'Tang',					None,					None,				None),
	('GiuongTrong',				'GiuongTrong',			None,					None,				None),
	('TamNgung',				'TamNgung',				None,					None,				None),
	('MoTa',					'MoTa',					None,					None,				None),
	('VatDungKemTheo',			'VatDungKemTheo',		None,					None,				None),
	('NgayTao_Key',				'NgayTao',				'DIM_Date',				'Date_Key',			'Ngay'),
	('NguoiTao_Id',				'NguoiTao_Id',			None,					None,				None),
	('NgayCapNhat_Key',			'NgayCapNhat',			'DIM_Date',				'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',			'NguoiCapNhat_Id',		None,					None,				None),
	('TrangThai_Key',			'TrangThai_Id',			None,					None,				None),
	('DungChung',				'DungChung',			None,					None,				None),
	('DichVuKhachHang_Id',		'DichVuKhachHang_Id',	None,					None,				None),
	('DichVuChamSoc_Id',		'DichVuChamSoc_Id',		None,					None,				None),
	('MaGiuongBHYT',			'MaGiuongBHYT',			None,					None,				None)
	# ('Source_Key',				'BenhVien_Key',			None,					None,				None)
]

DIM_TienTe = [ #13
	#TargetField			SourceField			ReferenceTable		ForeignKey			MapField
	('TienTe_Key',			None,					None,			None,				None),
	('TienTe_Id',			'TienTe_Id',			None,			None,				None),
	('TenTienTe',			'TenTienTe',			None,			None,				None),
	('TenTienTe_En',		'TenTienTe_En',			None,			None,				None),
	('TamNgung',			'TamNgung',				None,			None,				None),
	('NgayTao_Key',			'NgayTao',				'DIM_Date',		'Date_Key',			'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',			None,			None,				None),
	('NgayCapNhat_Key',		'NgayCapNhat',			'DIM_Date',		'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None,			None,				None)
	# ('Source_Key',			None,					'DIM_BenhVien',	'BenhVien_Key',		None)
]

DIM_LoaiGia = [ #14
	#TargetField			SourceField			ReferenceTable		ForeignKey				MapField
	('LoaiGia_Key',			None,				None,				None,					None),
	('LoaiGia_Id',			'LoaiGia_Id',		None,				None,					None),
	('MaLoaiGia',			'MaLoaiGia',		None,				None,					None),
	('TenLoaiGia',			'TenLoaiGia',		None,				None,					None),
	('TenLoaiGia_EN',		'TenLoaiGia_EN',	None,				None,					None),
	# ('NhomGia_Id',			'NhomGia_Id',		'Lst_Dictionary',	'Dictionary_Id',		None),
	# ('NhomGia_Code',		None,				'Lst_Dictionary',	'Dictionary_Code',		None),
	# ('NhomGia_Name',		None,				'Lst_Dictionary',	'Dictionary_Name',		None),
	# ('NhomGia_Name_En',		None,				'Lst_Dictionary',	'Dictionary_Name_En',	None),
	('CapTren_Id',			'CapTren_Id',		None,				None,					None),
	('GhiChu',				'GhiChu',			None,				None,					None),
	('TamNgung',			'TamNgung',			None,				None,					None),
	('NgayTao_Key',			'NgayTao',			'DIM_Date',			'Date_Key',				'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		None,				None,					None),
	('NgayCapNhat_Key',		'NgayCapNhat',		'DIM_Date',			'Date_Key',				'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,				None,					None),
	('Idx',					'Idx',				None,				None,					None)
	# ('Source_Key',			'BenhVien_Key',		None,				None,					None)
]

DIM_QuocGia = [ #15
	#TargetField			SourceField			ReferenceTable		ForeignKey			MapField
	('QuocGia_Key',			None,					None			,	None		,	None),
	('QuocGia_Id',			'Dictionary_Id',		None			,	None		,	None),
	('QuocGia_Code',		'Dictionary_Code',		None			,	None		,	None),	
	('QuocGia_Name',		'Dictionary_Name',		None			,	None		,	None),
	('QuocGia_Name_En',		'Dictionary_Name_En',	None			,	None		,	None),		
	('QuocGia_Name_Ru',		'Dictionary_Name_Ru',	None			,	None		,	None),		
	('Latin_Name',			'Latin_Name',			None			,	None		,	None),
	('NgayTao_Key',			'Creation_Date',		'DIM_Date'		,	'Date_Key'	,	'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',			None			,	None		,	None),
	('NgayCapNhat_Key',		'Last_Update_Date',		'DIM_Date'		,	'Date_Key'	,	'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None			,	None		,	None)
	#('Source_Key',			None					'DIM_BenhVien'		'BenhVien_Key'	None)
]

DIM_CongTy = [ #16
	#TargetField			SourceField			ReferenceTable		ForeignKey			MapField
	('Congty_Key',			None,					None,			None,				None),
	('Congty_Id',			'Congty_Id',			None,			None,				None),
	('MaCongty',			'MaCongty',				None,			None,				None),
	('TenCongty',			'TenCongty',			None,			None,				None),
	('TenCongty_En',		'TenCongty_En',			None,			None,				None),
	('TenCongty_Ru',		'TenCongty_Ru',			None,			None,				None),
	('DiaChi',				'DiaChi',				None,			None,				None),
	('DienThoai',			'DienThoai',			None,			None,				None),
	('Fax',					'Fax',					None,			None,				None),
	('Email',				'Email',				None,			None,				None),
	('MaSoThue',			'MaSoThue',				None,			None,				None),
	('GiamDoc',				'GiamDoc',				None,			None,				None),
	('NguoiLienHe',			'NguoiLienHe',			None,			None,				None),
	('NuocNgoai',			'NuocNgoai',			None,			None,				None),
	('NhaNuoc',				'NhaNuoc',				None,			None,				None),
	('TamNgung',			'TamNgung',				None,			None,				None),
	('TenKhongDau',			'TenKhongDau',			None,			None,				None),
	('NgayTao_Key',			'NgayTao',				'DIM_Date',		'Date_Key',			'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',			None,			None,				None),
	('NgayCapNhat_Key',		'NgayCapNhat',			'DIM_Date',		'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None,			None,				None),
	('HeSo',				'HeSo',					None,			None,				None),
	('DienThoai_LH',		'DienThoai_LH',			None,			None,				None),
	('NguoiLienHe2',		'NguoiLienHe2',			None,			None,				None),
	('DienThoai_LH2',		'DienThoai_LH2',		None,			None,				None)
]

DIM_KhoDuoc = [ #17
	#TargetField			SourceField			ReferenceTable		ForeignKey			MapField
	('KhoDuoc_Key',			None,				None,				None,				None),
	('KhoDuoc_Id',			'KhoDuoc_Id',		None,				None,				None),
	('MaKho',				'MaKho',			None,				None,				None),
	('TenKho',				'TenKho',			None,				None,				None),
	# ('PhongBan_Key',		'PhongBan_Id',		'DIM_PhongBan',		'PhongBan_Key',		'PhongBan_Id'),
	# ('LoaiKho',				'LoaiKho_Id',		'Lst_Dictionary',	'Dictionary_Id',	None),
	('TamNgung',			'TamNgung',			None,				None,				None),
	('TenKhongDau',			'TenKhongDau',		None,				None,				None),
	('NgayTao_Key',			'NgayTao',			'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',		None,				None,				None),
	('NgayCapNhat_Key',		'NgayCapNhat',		'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',	None,				None,				None),
	('QLNguon',				'QLNguon',			None,				None,				None),
	('KhoDuoc',				'KhoDuoc',			None,				None,				None),
	('KhoTaiSan',			'KhoTaiSan',		None,				None,				None),
	('KhoNHM',				'KhoNHM',			None,				None,				None),
	('KhoVPP',				'KhoVPP',			None,				None,				None),
	('KhoTTB',				'KhoTTB',			None,				None,				None),
	('TenKho_EN',			'TenKho_EN',		None,				None,				None),
	('TenKho_RU',			'TenKho_RU',		None,				None,				None)
]

DIM_NhaCungCap = [ #18
	#TargetField			SourceField				ReferenceTable		ForeignKey		MapField
	('KhoDuoc_Key',			None,						None,			None,			None),
	('NhaCungCap_Id',		'NhaCungCap_Id',			None,			None,			None),
	('MaNhaCungCap',		'MaNhaCungCap',				None,			None,			None),
	('TenNhaCungCap',		'TenNhaCungCap',			None,			None,			None),
	('TenNhaCungCap_En',	'TenNhaCungCap_En',			None,			None,			None),
	('TenNhaCungCap_Ru',	'TenNhaCungCap_Ru',			None,			None,			None),
	('DiaChi',				'DiaChi',					None,			None,			None),
	('DienThoai',			'DienThoai',				None,			None,			None),
	('Fax',					'Fax',						None,			None,			None),
	('Email',				'Email',					None,			None,			None),
	('MaSoThue',			'MaSoThue',					None,			None,			None),
	('GiamDoc',				'GiamDoc',					None,			None,			None),
	('NguoiLienHe',			'NguoiLienHe',				None,			None,			None),
	('NuocNgoai',			'NuocNgoai',				None,			None,			None),
	('NhaNuoc',				'NhaNuoc',					None,			None,			None),
	('TamNgung',			'TamNgung',					None,			None,			None),
	('TenKhongDau',			'TenKhongDau',				None,			None,			None),
	('NgayTao_Key',			'NgayTao',					'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',				None,			None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',				'DIM_Date',		'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',			None,			None,			None),
	('HeSo',				'HeSo',						None,			None,			None),
	('PH_Duoc',				'PH_Duoc',					None,			None,			None),
	('PH_NHM',				'PH_NHM',					None,			None,			None),
	('PH_TaiSan',			'PH_TaiSan',				None,			None,			None),
	('LoaiHinhCongTy',		'LoaiHinhCongTy_Id',		None,			None,			None),
	('Intercompany',		'Intercompany',				None,			None,			None),
	('tentat',				'tentat',					None,			None,			None),
	('idx',					'idx',						None,			None,			None),
	('TrangThai',			'TrangThai',				None,			None,			None),
	('DonVi',				'DonVi',					None,			None,			None)
]

DIM_CoSoThuoc = [ #19
	#TargetField			SourceField				ReferenceTable		ForeignKey		MapField
	('CoSoThuoc_Key',		None,					None,				None,			None),
	('CoSoThuoc_Id',		'CoSoThuoc_Id',			None,				None,			None),
	# ('KhoDuoc_Key',			'KhoDuoc_Id',			'DIM_KhoDuoc',		'KhoDuoc_Key',	'KhoDuoc_Id'),
	# ('Duoc_Key',			'Duoc_Id',				'DIM_Duoc',			'Duoc_Key',		'Duoc_Id'),
	('SoLuongMin',			'SoLuongMin',			None,				None,			None),
	('SoLuongMax',			'SoLuongMax',			None,				None,			None),
	('TamNgung',			'TamNgung',				None,				None,			None),
	('NgayTao_Key',			'NgayTao',				'DIM_Date',			'Date_Key',		'Ngay'),
	('NguoiTao_Id',			'NguoiTao_Id',			None,				None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',			'DIM_Date',			'Date_Key',		'Ngay'),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None,				None,			None)
	# ('Source_Key',			None,					'DIM_BenhVien',		'BenhVien_Key',	None)
]

DIM_DichVu_DonGia = [ #20
	#TargetField			SourceField				ReferenceTable		ForeignKey		MapField
	('DichVu_DonGia_Key',	None,					None,				None,			None),
	('DichVu_DonGia_Id',	'DichVu_DonGia_Id',		None,				None,			None),
	('BangGia_Id',			'BangGia_Id',			None,				None,			None),
	('DichVu_Key',			'DichVu_Id',			'DIM_DichVu',		'DichVu_Key',	'DichVu_Id'),
	('LoaiGia_Key',			'LoaiGia_Id',			'DIM_LoaiGia',		'LoaiGia_Key',	'LoaiGia_Id'),
	('TienTe_Key',			'TienTe_Id',			'DIM_TienTe',		'TienTe_Key',	'DIM_TienTe'),
	('DonGia',				'DonGia',				None,				None,			None),
	('DonGiaThapNhat',		'DonGiaThapNhat',		None,				None,			None),
	('DonGiaCaoNhat',		'DonGiaCaoNhat',		None,				None,			None),
	('TyLeVAT',				'TyLeVAT',				None,				None,			None),
	('GiaTriVAT',			'GiaTriVAT',			None,				None,			None),
	('TrangThai',			'TrangThai',			None,				None,			None),
	('TamNgung',			'TamNgung',				None,				None,			None),
	('NgayTao_Key',			'NgayTao',				'DIM_Date',			'Date_Key',		None),
	('NguoiTao_Id',			'NguoiTao_Id',			None,				None,			None),
	('NgayCapNhat_Key',		'NgayCapNhat',			'DIM_Date',			'Date_Key',		None),
	('NguoiCapNhat_Id',		'NguoiCapNhat_Id',		None,				None,			None)
	# ('Source_Key',			None,					'DIM_BenhVien',		'BenhVien_Key',	None)
]

DIM_Duoc_DonGia = [ #21
	#TargetField				SourceField					ReferenceTable		ForeignKey			MapField
	('Duoc_DonGia_Key',			None,						None,				None,				None),
	('Duoc_DonGia_Id',			'Duoc_DonGia_Id',			None,				None,				None),
	('BangGia_Id',				'BangGia_Id',				None,				None,				None),
	('Duoc_Key',				'Duoc_Id',					'DIM_Duoc',			'Duoc_Key',			'Duoc_Id'),
	('LoaiGia_Key',				'LoaiGia_Id',				'DIM_LoaiGia',		'LoaiGia_Key',		'LoaiGia_Id'),
	('TienTe_Key',				'TienTe_Id',				'DIM_TienTe',		'TienTe_Key',		'TienTe_Id'),
	('DonGia',					'DonGia',					None,				None,				None),
	('TyLeVAT',					'TyLeVAT',					None,				None,				None),
	('GiaTriVAT',				'GiaTriVAT',				None,				None,				None),
	('TrangThai',				'TrangThai',				None,				None,				None),
	('TamNgung',				'TamNgung',					None,				None,				None),
	('NgayTao_Key',				'NgayTao',					'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiTao_Id',				'NguoiTao_Id',				None,				None,				None),
	('NgayCapNhat_Key',			'NgayCapNhat',				'DIM_Date',			'Date_Key',			'Ngay'),
	('NguoiCapNhat_Id',			'NguoiCapNhat_Id',			None,				None,				None),
	('GiaVonTB',				'GiaVonTB',					None,				None,				None),
	('TyLeLai',					'TyLeLai',					None,				None,				None),
	('DonGiaBanGoc_SauVAT',		'DonGiaBanGoc_SauVAT',		None,				None,				None),
	('DonGiaBanGoc_TruocVAT',	'DonGiaBanGoc_TruocVAT',	None,				None,				None),
	('GiaVonGanNhat',			'GiaVonGanNhat',			None,				None,				None)
	# ('Source_Key',				None,						'DIM_BenhVien',		'BenhVien_Key',		None)
]

