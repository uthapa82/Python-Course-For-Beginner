def sandwich_list(*sandwich_names):
    for sandwich_name in sandwich_names:
        print(sandwich_name.title() + " sandwich has been ordered.")

def main():
    sandwich_list('nutella')
    sandwich_list('veg', 'cheesi')
    sandwich_list('chicken', 'grilled')
    
if __name__ == '__main__':
    main()



