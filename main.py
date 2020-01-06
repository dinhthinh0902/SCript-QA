import os
import sys
HOME_DIR = '/home/nminh/Jupyter/'

sys.path.insert(0, os.path.abspath(HOME_DIR + '/mapping'))
sys.path.insert(0, os.path.abspath(HOME_DIR + '/run'))
import mapping
import run

def test_flow():
    table_list = [
        'DIM_NhomDichVu',
        'DIM_DichVu',
        'DIM_DonViTinh',
        'DIM_LoaiVatTu',
        'DIM_ICD',
        'DIM_Duoc',
        'DIM_PhanNhomDuoc',
        'DIM_LoaiDuoc',
        'DIM_DonViHanhChinh',
        'DIM_BenhNhan',
        'DIM_PhongBan',
        'DIM_GiuongBenh',
        'DIM_TienTe',
        'DIM_LoaiGia',
        'DIM_QuocGia',
        'DIM_CongTy',
        'DIM_KhoDuoc',
        'DIM_NhaCungCap',
        'DIM_CoSoThuoc',
        'DIM_DichVu_DonGia',
        'DIM_Duoc_DonGia',
        'DIM_KSK_BenhNhan',
        'DIM_KSK_HopDong',
        'DIM_KSK_HopDong_DichVu',
        'DIM_NhanVien',
        'DIM_NguonDuoc',
        'DIM_DuocKyTonKho',
        'DIM_ThietBi',
        'DIM_BenhVien',
        'DIM_CheDoAnUong',
        'DIM_CheDoChamSoc',
        'DIM_LyDoTiepNhan',
        'DIM_HinhThucDenKham',
        'DIM_NgheNghiep',
        'DIM_DanToc',
        'DIM_HangSanXuat',
        'DIM_PhanLoaiKetQua',
        'DIM_GiaiQuyetKhamBenh',
        'DIM_LyDoNhapVien',
        'DIM_LoaiBenhAn',
        'DIM_KipMo_VaiTro',
        'DIM_TienTe_TyGia',
        'DIM_DuocCoSoThuoc'
    ]
    for item in table_list:
        print('\n======= test_result_of: ' + item + ' =======')
        print('\n--TC_001')
        print(run.TC_001_verify_table_structure(item))
        print('\n--TC_002')
        print(run.TC_002_verify_initial_load_data_loaded_fully(item))
        print('\n--TC_003')
        print(run.TC_003_verify_initial_source_key(item))
        print('\n--TC_004')
        print(run.TC_004_verify_initial_data_in_each_column(item))
        print('\n--TC_005')
        print(run.TC_005_verify_initial_foreign_key(item))
        print('\n=============================================')

if __name__ == '__main__':
    test_flow()
    run.print_summary()
    # print(run.TC_002_count_data_loaded_of('DIM_DichVu'));
    # run.read_table('DM_LoaiVatTu')
    # run.read_table('DM_QuocGia')
    #print(mapping.DIM_ICD[0])

#---Note------------------------------------------------------------------
#exec a string as command in python
#exec('print(mapping.' + table_list[0] + '[0])') #mapping.DIM_ICD[]


