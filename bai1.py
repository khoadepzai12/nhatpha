# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:03:05 2024

@author: Administrator
"""

import requests
def display_student_list(student_data):
    print("danh sach sinh vien: ")
    for student in student_data:
        print(f"MSSV: {student['MSSV']},Name: {student['Name']},Gender: {student['Gender']}, Birthday: {student['Birthday']}, City: {student['City']}")
def query_student(student_data,mssv):
    student=next((s for s in student_data if s['MSSV']==mssv),None)
    if student:
        print("thong tin cua sinh vien: ")
        print(f"MSSV: {student['MSSV']}")
        print(f"Name: {student['Name']}")
        print(f"Gender: {student['Gender']}")
        print(f"Birthday: {student['Birthday']}")
        print(f"City: {student['City']}")
    else:
        print("khong tim thay sinh vien co MSSV nay")
def add_student(student_data,new_student):
   student_data.append(new_student)
   print("sinh vien da duoc them vao danh sach")
def delete_student(student_data,mssv):
    for student in student_data:
        if student['MSSV']==mssv: 
            student_data.remove(student)
            print("sinh vien da duoc xoa khoi danh sach")
            return
        print("khong tim thay sinh vien co MSSV")
def update_student(student_data,mssv,new_info):
    student=next((s for s in student_data if s['MSSV']==mssv),None)
    if student:
        student.update(new_infor)
        print("thong tin da duoc them")
    else:
        print("khong tin thay sinh vien")

def main():
    url="https://v1.slashapi.com/5-4/mysql/57i3uDerJ2/students"
    response=requests.get(url)
    if response.status_code==200:
        student_data=response.json()['data']
    else:
        print("khong the lay danh sach sinh vien tu API.")
        return
if __name__=="__main__":
    main()