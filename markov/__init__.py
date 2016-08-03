# -*- coding: utf-8 -*-
import parse
import storage
import generator

if __name__ == "__main__":
    st = storage.Storage()
    p = parse.Parser(st)
    gen = generator.Generator(st)
    f = open('file.txt', 'r+', encoding='utf-8')
    text = ' '.join(f.readlines())
    f.close()
    p.split_sentences(text)
    # t = 0
    # for i in p.get_sentences():
    #     print('{}: {}'.format(t, i.strip()))
    #     t += 1
    words = p.build_tree()
    st.add_pair(('собака', 'сидит', 500))
    st.add_pair(('собаки', 'сидят', 500))
    st.save_file()
    # st.read_file()
    while True:
        print(gen.generate_sentence())
        s = input()
        if s == 'q':
            break
    # st.output()