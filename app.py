import streamlit as st

st.set_page_config(page_title="Penghitung Rata-rata")

st.title("Aplikasi Penghitung Rata-rata Sederhana")
st.write("Masukkan angka-angka yang ingin dihitung rata-ratanya, pisahkan dengan koma (,).")

# Input teks dari pengguna
numbers_input = st.text_input("Masukkan angka (contoh: 10,20,30,40,50)", "10,20,30")

# Tombol untuk memicu perhitungan
if st.button("Hitung Rata-rata"):
    if not numbers_input:
        st.error("Mohon masukkan angka. Input tidak boleh kosong.")
    else:
        try:
            # Memisahkan string angka menjadi list string, lalu mengubahnya menjadi float
            # Menggunakan float agar bisa menghitung rata-rata desimal
            numbers_list = [float(num.strip()) for num in numbers_input.split(',')]

            if not numbers_list:
                st.error("Tidak ada angka yang valid ditemukan setelah parsing. Mohon masukkan angka yang benar.")
            else:
                # Menghitung rata-rata
                average = sum(numbers_list) / len(numbers_list)

                st.success(f"Rata-rata dari angka-angka Anda adalah: **{average:.2f}**")
                st.write(f"Angka yang Anda masukkan: {numbers_list}")
                st.info("Aplikasi ini berjalan di dalam Docker container!")

        except ValueError:
            st.error("Input tidak valid. Pastikan semua adalah angka yang dipisahkan koma.")
        except Exception as e:
            st.error(f"Terjadi kesalahan tak terduga: {str(e)}")

st.markdown("---")
st.write("Dibuat dengan Streamlit dan Docker.")