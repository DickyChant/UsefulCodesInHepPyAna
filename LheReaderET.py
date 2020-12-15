import xml.etree.ElementTree as ET
from ROOT import std,TTree,TFile
from array import array

def main(input,output):

    #---------------------------------------------------------
    # Set up arrays for holding event info to be written to branches
    #---------------------------------------------------------
    m_num_particles = array('i',[0])
    m_event_weight = array('f',[0.0])
    m_event_scale = array('f',[0.0])
    m_alpha_em = array('f',[0.0])
    m_alpha_s = array('f',[0.0])

    m_pdgid = std.vector('int')()
    m_status = std.vector('int')()
    m_mother1 = std.vector('int')()
    m_mother2 = std.vector('int')()
    m_color1 = std.vector('int')()
    m_color2 = std.vector('int')()
    m_px = std.vector('float')()
    m_py = std.vector('float')()
    m_pz = std.vector('float')()
    m_e = std.vector('float')()
    m_m = std.vector('float')()
    m_tau = std.vector('float')()
    m_spin = std.vector('float')()

    #---------------------------------------------------------
    # Set up TTree and branches for storing info
    #---------------------------------------------------------
    out_file = TFile(output,'recreate')
    my_tree = TTree('mytree','tree of generated events')

    my_tree.Branch('numParticles',m_num_particles,'numParticles/I')
    my_tree.Branch('eventWeight',m_event_weight,'eventWeight/F')
    my_tree.Branch('eventScale',m_event_scale,'eventScale/F')
    my_tree.Branch('alphaEM',m_alpha_em,'alphaEM/F')
    my_tree.Branch('alphaS',m_alpha_s,'alphaS/F')
    my_tree.Branch('pdgID',m_pdgid)
    my_tree.Branch('pdgStatus',m_status)
    my_tree.Branch('mother1',m_mother1)
    my_tree.Branch('mother2',m_mother2)
    my_tree.Branch('color1',m_color1)
    my_tree.Branch('color2',m_color2)
    my_tree.Branch('px',m_px)
    my_tree.Branch('py',m_py)
    my_tree.Branch('pz',m_pz)
    my_tree.Branch('E',m_e)
    my_tree.Branch('Mass',m_m)
    my_tree.Branch('Tau',m_tau)
    my_tree.Branch('Spin',m_spin)

    inLHE = ET.parse(input)
    root = inLHE.getroot()
    for child in root:
        if child.tag != "event":
            continue
        for line in child.text.split('\n'):
            if line == "\n":
                continue
            if len(line) == 0:
                continue
            element = line.split()
            if len(element) == 6:
                m_num_particles[0] = int(element[0])
                m_event_weight[0] = eval(element[2])
                m_event_scale[0] = eval(element[3]) 
                m_alpha_em[0] = eval(element[4])
                m_alpha_s[0] = eval(element[5])
            if len(element) == 13:
                m_pdgid.push_back(int(element[0]))
                m_status.push_back(int(element[1]))
                m_mother1.push_back(int(element[2]))
                m_mother2.push_back(int(element[3]))
                m_color1.push_back(int(element[4]))
                m_color2.push_back(int(element[5]))
                m_px.push_back(eval(element[6]))
                m_py.push_back(eval(element[7]))
                m_pz.push_back(eval(element[8]))
                m_e.push_back(eval(element[9]))
                m_m.push_back(eval(element[10]))
                m_tau.push_back(eval(element[11]))
                m_spin.push_back(eval(element[12]))
            if len(element) == 16:
                my_tree.Fill()
                
                m_pdgid.clear()
                m_status.clear()
                m_mother1.clear()
                m_mother2.clear()
                m_color1.clear()
                m_color2.clear()
                m_px.clear()
                m_py.clear()
                m_pz.clear()
                m_e.clear()
                m_m.clear()
                m_tau.clear()
                m_spin.clear()
    
    out_file.Write()
    out_file.Close()

            
                


if __name__ == "__main__":
    main("herwig.lhe","herwig.root")
    main("pythia.lhe","pythia.root")