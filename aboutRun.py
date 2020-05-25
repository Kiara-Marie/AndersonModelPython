import config

def about_run(W, iterations, num_sites, max_t, jComputer, energy_computer, file_prefix):
  str_list = []
  str_list.append("%d iterations for %d sites with W = %d\n" %(iterations,num_sites, W))
  str_list.append(energy_computer.desc)
  str_list.append(jComputer.desc)
  if (config.SAVE):
    my_file = open(file_prefix + "AboutRun.txt","w")
    my_file.write(''.join(str_list)) 