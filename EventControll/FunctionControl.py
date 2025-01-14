# -*- coding: utf-8 -*-
from Window.Info_Window import *
from Container.Container import *
from Window.Ui_DeleteCode import *
from Window.Ui_InputText import *


class FucntionControl:
    def __init__(self, window):
        self.window = window
        self.initProject()

    def initProject(self):
        self.companyContainer = Container(self.window)

#회사 입력 버튼 클리어!
    def btn_insert(self):
        company = self.companyContainer.getCompany()
        if len(company.company) > 0 and len(company.job) > 0 and len(company.sales) > 0:
            input_data(company)

#업데이트 버튼 클리어! /위에 창 업데이트 + 리스트 수정만 해주면 됨.
    def btn_update(self):
        company = self.companyContainer.getCompany()
        index = self.getSelectRowIndex()
        if len(company.company) > 0 and len(company.job) > 0 and len(company.sales) > 0:
            remove(self.companyContainer.companyList[index])
            input_data(company)
            self.companyContainer.refreshContainer()

    #클릭시 위에 창 업데이트 해야하는거 민수형 파일 이용
    def btn_listviewItemClick(self):
        index = self.getSelectRowIndex()
        self.companyContainer.companyInfo.makeUpEditText(self.companyContainer.companyList[index])

    #삭제 버튼 클리어! (선택한거)
    def btn_delete(self):
        self.btn_openDelete()
        #remove(self.companyContainer.getCompany())
        #self.companyContainer.refreshContainer()

    # 새로 고침 버튼 클릭시
    def btn_refresh(self):
        self.companyContainer.refreshContainer()

    # 회사 정보 창 오픈
    def btn_openInfo(self):
        self.dialog = QtWidgets.QMainWindow()
        self.dialog.ui = Info_Window(self.dialog,self.companyContainer.getCompany())
        self.dialog.show()

    # 삭제 코드 창 오픈
    def btn_openDelete(self):
        import firebase_admin
        from firebase_admin import db
        from firebase_admin import credentials
        cred = credentials.Certificate({
          "type": "service_account",
          "project_id": "analysis-for-company",
          "private_key_id": "2044da0542bb11ae463955fd5865d20f741668f1",
          "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDQHIXZ3zrUKJR6\nwk4wgNkLWUfMBtPRHasWg2epS6DtCGRUqJ/tX2Jy7y1+2acxkvC4tbUmnBNQCEaI\nMgbm1tHjAPDsVHfEUfektCyXlt7hrbbh/XEq+Jh3PLTT9ZS8aTXgt+NdgD8+EkFv\nXit5zDqTrOvvgl3Y1jG3idnFEN6Hbg72KvGsfOn40GUYzPdpqjlIaLYuRvdiNLXr\n57+FhPvdBIZiQB+06RFWLImiySEA6Vzk/PFUdnb/QDVbsI3im06eDp/5AJM56vhX\nCsaHqkY28cup8DpX/Um0PTVtXRCJZuc74MSPgRvIbzXmBk3s/zciWSY7JTHYa4rm\nC21T9epjAgMBAAECggEALum3HLGPK+NH8VJa2OE6zC2gmzQQzKuQ9T7C/+1eBgDl\nyRXIE3T0lu8mxNkgsPKsVB8WCnGVgu2SpMIOPzw+zRrZtJSn+Pf3SMga40Mt1Bba\nSqBcwfCPQhXLt5o9IKng7NrXJK0z1HS+DnJef5LTw5VwDCpJqIdEZtjq39sZJtL2\n4KvE043/6IS2nXGAZDmY1I52hoQwptD+jNmMHbd895Xbjk05tqBEY5jyTohwJu7p\n0ex1HJI+ntMnqydnMDR2NHNkQbJLxCdk0y/NlVx0F6/Ya+QoTXwSteDIXpFE0TQM\nhrssiQ3xok8ayRikUDqMeVi2kGXv627joJILvSkaUQKBgQDw5eBpXGh9/dSRD92l\nqxJgTj0ElI07YP57H2sGsiJ9R22rCXu5BELOsEATe7a7owRyOZa2WBDmAUG+8OxR\nheW72mzPilRYsm8mnIh78m1E71Kr/2q1dV+DAdff58tA/FzHTpF3KuFw8//PFlRl\nS7FobhQqwbZY69e9f1a/px7lEwKBgQDdKHYshOHXT83CM4sNRIha5wAeyV/rNPyA\nr8XAttWjU+jIXpWql/lo+NnpyO52ZOKSrdrrMnjmxltMlvy4XtRS79OIwsZeektG\nObj9/2HfLxGDxsG23cZzdgqZQsIAuHU+k3ENo2DrDYlZYN0/mDNGNfXGroJ3V4f1\nF6jdIkSfcQKBgEcD/XwR+dvqkFeTTcwg+nHZnrNS96+hkGPLh0maCgDUpcfeK9MH\nJoq3+qvDtMLr88uYno1yuMiVZkRb0c7WojsW0Sz9oo/jSlEfpDyl4wCHbN+3lEWa\nLGX6jSE8u/aUbuVyi/+NbJhX1fm+o3KZNduLV/ai1JayMA91EqW9JqZxAoGAPWq3\nJrXgYgLviTb3LsARfe0Yw3P5B0C3vqURresYeTscMkjSF4YM5XH2Uk5Sqt5pbYKK\ngTaLDMuZHzPvCuSK4l1nyVsN677amK3/CcqaS3iuzIGt2jLModPuLZG0fq67IJ2h\nj8AHcj9YHVIhH0ANPTpO/tYHtUzBnPbtFjwmAoECgYACwgA1XTX9KPhD6EM7ANdI\nv8OBZ3ftmaQHo+dO87wtwVb5yZZOZrftnvSmt/ERGkOFB7qN8netP+eHBGHxSPPx\n/AgVYMGkPOnQlEWIOtI4TubwjvsTeyHtmMsI5sFSsi+eoCNBk8MmkoLugx97IOAk\nMK0fFz/owEwzoUZSFSGu7w==\n-----END PRIVATE KEY-----\n",
          "client_email": "firebase-adminsdk-7tnqu@analysis-for-company.iam.gserviceaccount.com",
          "client_id": "103197426300283058233",
          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
          "token_uri": "https://oauth2.googleapis.com/token",
          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
          "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7tnqu%40analysis-for-company.iam.gserviceaccount.com"})
                
        s = "passwd"
        ref = db.reference(s)
        print("입력된것:",ref.get())

        print(Ui_DeleteCode())
        if(str(ref.get())==str(Ui_DeleteCode())):
            print("삭제 되었음")
            return True
        else:
            print("삭제 불가능")
            return False


    # 입력 확장 버튼 클릭
    def btn_openInput(self):
        a = Ui_InputText()


    # 로우 선택 시
    def getSelectRowIndex(self):
        index = self.window.tableWidget.selectionModel().currentIndex().row()
        return index
