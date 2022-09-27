import printing_functions as p
import calculate_grade 

def main():
    p.print_models("Tesla Cars ")
    p.show_uncomplete_models('Rivian Cars')
    calculate_grade.generate_result()

if __name__ == '__main__':
    main()