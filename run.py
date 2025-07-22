import os
from configs.config import get_args
from utils.visualize import display_args

def main():
    
    # get configuration
    args = get_args()
    
    # display config
    display_args(args)
    
    # 

if __name__ == '__main__':
    main()