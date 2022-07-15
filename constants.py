import monai
import torch

from pathlib import Path


class Constants:
    def __init__(self):
        # Paths
        self.best_metrics = Path('./best_metrics')
        self.dataset_path = Path('./data')
        self.logs = Path('./logs')

        self.masks = Path('./ProstateX_masks')
        self.plotting = Path('./ProstateX_plotting')

        self.processed = self.dataset_path / 'processed'
        self.unprocessed = self.dataset_path / 'unprocessed'

        # Path to data converted using MRIcoGL
        self.unprocessed_nifti = self.unprocessed / 'NIFTI'
        # Path to KTrans data (*.mhd)
        self.unprocessed_ktrans = self.unprocessed / 'KTrans'

        self.findings = self.dataset_path / 'ProstateX-Findings-Train.csv'
        self.labels_pkl = self.processed / 'lesion_findings.pickle'

        # Training and testing parameters
        self.split_ratio = 0.8
        self.image_resize = 168

        self.batch_size = 2
        self.batch_size_test = 1
        self.num_workers = 0
        self.epochs = 50

        self.spatial_dims = 3
        self.in_channels = 1
        self.out_channels = 2
        self.lr = 1e-4

        self.model = monai.networks.nets.DenseNet121(
            spatial_dims=self.spatial_dims,
            in_channels=self.in_channels,
            out_channels=self.out_channels
        )
        self.loss_function = torch.nn.BCEWithLogitsLoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), self.lr)

        # Information used for logging
        self.model_type = f'DensNet121({self.spatial_dims}, {self.in_channels}, {self.out_channels})'
        self.loss_type = f'Binary Cross Entropy'
        self.optimizer_type = f'Adam'
