from pathlib import Path


class Patient:
    def __init__(self):
        self.ProxID = str
        self.num_id = int
        self.ClinSig = []
        self.fid = []
        self.pos = []
        self.zone = []
        self.spacing = None
        self.slices = None
        self.T2 = []
        self.ADC = []
        self.DWI = []
        self.KTrans = Path

    def add_labels(self, labels):
        self.ProxID = labels.ProxID
        self.num_id = self.get_patient_index()
        self.ClinSig = labels.ClinSig
        self.fid = labels.fid
        self.pos = labels.pos
        self.zone = labels.zone
        self.spacing = labels.spacing
        self.slices = labels.slices
        self.T2 = labels.T2
        self.ADC = labels.ADC
        self.DWI = labels.DWI
        self.KTrans = labels.KTrans

    def set_patient_pid(self, filename):
        self.ProxID = filename[:14]
        self.num_id = self.get_patient_index()

    def get_patient_index(self):
        return int(self.ProxID[10:])

    def add_path(self, image_type, path):
        if image_type == 'T2':
            self.T2.append(path)
        elif image_type == 'ADC':
            self.ADC.append(path)
        elif image_type == 'DWI':
            self.DWI.append(path)
        elif image_type == 'KTrans':
            self.KTrans = path

    def add_lesion_data(self, findings, lesions_info):
        self.ClinSig.append(findings.ClinSig)
        self.fid.append(findings.fid)
        self.pos.append(findings.pos)
        self.zone.append(findings.zone)

        # voxel spacing and slices containing prostate lesion
        self.spacing = lesions_info.spacing
        self.slices = lesions_info.fg_slices

    def get_dataframe_row(self):
        return [
            self.ProxID, self.ClinSig, self.fid, self.pos, self.zone,
            self.spacing, self.slices,
            self.T2, self.ADC, self.DWI, self.KTrans
        ]

