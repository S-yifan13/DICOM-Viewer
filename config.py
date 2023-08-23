# request
BACKEND_BASE_URL = 'http://127.0.0.1:8000/api'
CHECK_MODEL_URL = 'http://10.212.253.234:8611/predict'
SEGMENTATION_MODEL_URL = 'http://10.212.253.234:8612/segmentation'

# path
TEMP_DIR = 'temp'
DATA_DIR = 'data'
TEMP_CHECK_DIR = TEMP_SEG_DIR = 'temp/check/'

# args
MIN_CHECK_SHOW_RATIO = 0.7
IMAGE_WIDTH = 615
CHECK_BATCH_SIZE = 30
SEG_BATCH_SIZE = 10
NIDUS_TYPE = ['js', 'kq', 'xs']
NIDUS_SEG = ['纤维斑块', '钙化斑块', '带薄纤维帽的脂质池']