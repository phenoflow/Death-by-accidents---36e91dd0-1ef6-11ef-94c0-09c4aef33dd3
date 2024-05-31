cwlVersion: v1.0
steps:
  read-potential-cases-i2b2:
    run: read-potential-cases-i2b2.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule1
  death-by-accidents-unnatural-cause-noncolln---secondary:
    run: death-by-accidents-unnatural-cause-noncolln---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule2
      potentialCases:
        id: potentialCases
        source: read-potential-cases-i2b2/output
  death-by-accidents-unnatural-cause-explosure---secondary:
    run: death-by-accidents-unnatural-cause-explosure---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule3
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-noncolln---secondary/output
  death-by-accidents-unnatural-cause-waterski---secondary:
    run: death-by-accidents-unnatural-cause-waterski---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule4
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-explosure---secondary/output
  death-by-accidents-unnatural-cause-23wheel---secondary:
    run: death-by-accidents-unnatural-cause-23wheel---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule5
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-waterski---secondary/output
  death-by-accidents-unnatural-cause-scratched---secondary:
    run: death-by-accidents-unnatural-cause-scratched---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule6
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-23wheel---secondary/output
  death-by-accidents-unnatural-cause-handgun---secondary:
    run: death-by-accidents-unnatural-cause-handgun---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule7
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-scratched---secondary/output
  death-by-accidents-unnatural-cause-nontraf---secondary:
    run: death-by-accidents-unnatural-cause-nontraf---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule8
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-handgun---secondary/output
  death-by-accidents-unnatural-cause-indust---secondary:
    run: death-by-accidents-unnatural-cause-indust---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule9
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-nontraf---secondary/output
  death-by-accidents-unnatural-cause-fixedwing---secondary:
    run: death-by-accidents-unnatural-cause-fixedwing---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule10
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-indust---secondary/output
  death-by-accidents-unnatural-cause-hallucn---secondary:
    run: death-by-accidents-unnatural-cause-hallucn---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule11
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-fixedwing---secondary/output
  death-by-accidents-unnatural-cause-boiler---secondary:
    run: death-by-accidents-unnatural-cause-boiler---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule12
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-hallucn---secondary/output
  death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary:
    run: death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule13
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-boiler---secondary/output
  gastric-death-by-accidents-unnatural-cause---secondary:
    run: gastric-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule14
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary/output
  death-by-accidents-unnatural-cause-light---secondary:
    run: death-by-accidents-unnatural-cause-light---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule15
      potentialCases:
        id: potentialCases
        source: gastric-death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-furniture---secondary:
    run: death-by-accidents-unnatural-cause-furniture---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule16
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-light---secondary/output
  death-by-accidents-unnatural-cause-drowng---secondary:
    run: death-by-accidents-unnatural-cause-drowng---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule17
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-furniture---secondary/output
  death-by-accidents-unnatural-cause-persons---secondary:
    run: death-by-accidents-unnatural-cause-persons---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule18
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-drowng---secondary/output
  death-by-accidents-unnatural-cause-flood---secondary:
    run: death-by-accidents-unnatural-cause-flood---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule19
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-persons---secondary/output
  death-by-accidents-unnatural-cause-steps---secondary:
    run: death-by-accidents-unnatural-cause-steps---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule20
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-flood---secondary/output
  death-by-accidents-unnatural-cause-hcarbon---secondary:
    run: death-by-accidents-unnatural-cause-hcarbon---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule21
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-steps---secondary/output
  death-by-accidents-unnatural-cause-spine---secondary:
    run: death-by-accidents-unnatural-cause-spine---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule22
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-hcarbon---secondary/output
  death-by-accidents-unnatural-cause-tsport---secondary:
    run: death-by-accidents-unnatural-cause-tsport---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule23
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-spine---secondary/output
  death-by-accidents-unnatural-cause-sailboat---secondary:
    run: death-by-accidents-unnatural-cause-sailboat---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule24
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-tsport---secondary/output
  death-by-accidents-unnatural-cause-shotgun---secondary:
    run: death-by-accidents-unnatural-cause-shotgun---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule25
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-sailboat---secondary/output
  death-by-accidents-unnatural-cause-specif---secondary:
    run: death-by-accidents-unnatural-cause-specif---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule26
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-shotgun---secondary/output
  death-by-accidents-unnatural-cause-animaldrawn---secondary:
    run: death-by-accidents-unnatural-cause-animaldrawn---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule27
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-specif---secondary/output
  death-by-accidents-unnatural-cause-hanging---secondary:
    run: death-by-accidents-unnatural-cause-hanging---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule28
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-animaldrawn---secondary/output
  death-by-accidents-unnatural-cause-clothing---secondary:
    run: death-by-accidents-unnatural-cause-clothing---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule29
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-hanging---secondary/output
  death-by-accidents-unnatural-cause-injuring---secondary:
    run: death-by-accidents-unnatural-cause-injuring---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule30
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-clothing---secondary/output
  material-death-by-accidents-unnatural-cause---secondary:
    run: material-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule31
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-injuring---secondary/output
  death-by-accidents-unnatural-cause-mcycle---secondary:
    run: death-by-accidents-unnatural-cause-mcycle---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule32
      potentialCases:
        id: potentialCases
        source: material-death-by-accidents-unnatural-cause---secondary/output
  environmental-death-by-accidents-unnatural-cause---secondary:
    run: environmental-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule33
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-mcycle---secondary/output
  death-by-accidents-unnatural-cause-falling---secondary:
    run: death-by-accidents-unnatural-cause-falling---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule34
      potentialCases:
        id: potentialCases
        source: environmental-death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-noncoll---secondary:
    run: death-by-accidents-unnatural-cause-noncoll---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule35
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-falling---secondary/output
  death-by-accidents-unnatural-cause-skateboard---secondary:
    run: death-by-accidents-unnatural-cause-skateboard---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule36
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-noncoll---secondary/output
  death-by-accidents-unnatural-cause-objects---secondary:
    run: death-by-accidents-unnatural-cause-objects---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule37
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-skateboard---secondary/output
  death-by-accidents-unnatural-cause-kayak---secondary:
    run: death-by-accidents-unnatural-cause-kayak---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule38
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-objects---secondary/output
  death-by-accidents-unnatural-cause-scorpion---secondary:
    run: death-by-accidents-unnatural-cause-scorpion---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule39
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-kayak---secondary/output
  death-by-accidents-unnatural-cause-dagger---secondary:
    run: death-by-accidents-unnatural-cause-dagger---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule40
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-scorpion---secondary/output
  death-by-accidents-unnatural-cause-insect---secondary:
    run: death-by-accidents-unnatural-cause-insect---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule41
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-dagger---secondary/output
  death-by-accidents-unnatural-cause-storm---secondary:
    run: death-by-accidents-unnatural-cause-storm---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule42
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-insect---secondary/output
  death-by-accidents-unnatural-cause-suffocation---secondary:
    run: death-by-accidents-unnatural-cause-suffocation---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule43
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-storm---secondary/output
  death-by-accidents-unnatural-cause-sequelae---secondary:
    run: death-by-accidents-unnatural-cause-sequelae---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule44
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-suffocation---secondary/output
  death-by-accidents-unnatural-cause-spider---secondary:
    run: death-by-accidents-unnatural-cause-spider---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule45
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-sequelae---secondary/output
  death-by-accidents-unnatural-cause-hornet---secondary:
    run: death-by-accidents-unnatural-cause-hornet---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule46
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-spider---secondary/output
  death-by-accidents-unnatural-cause-firework---secondary:
    run: death-by-accidents-unnatural-cause-firework---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule47
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-hornet---secondary/output
  death-by-accidents-unnatural-cause-pinched---secondary:
    run: death-by-accidents-unnatural-cause-pinched---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule48
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-firework---secondary/output
  death-by-accidents-unnatural-cause-avalanche---secondary:
    run: death-by-accidents-unnatural-cause-avalanche---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule49
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-pinched---secondary/output
  death-by-accidents-unnatural-cause-antirheum---secondary:
    run: death-by-accidents-unnatural-cause-antirheum---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule50
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-avalanche---secondary/output
  death-by-accidents-unnatural-cause-motion---secondary:
    run: death-by-accidents-unnatural-cause-motion---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule51
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-antirheum---secondary/output
  death-by-accidents-unnatural-cause-ladder---secondary:
    run: death-by-accidents-unnatural-cause-ladder---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule52
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-motion---secondary/output
  death-by-accidents-unnatural-cause-streetcar---secondary:
    run: death-by-accidents-unnatural-cause-streetcar---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule53
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-ladder---secondary/output
  death-by-accidents-unnatural-cause-orifice---secondary:
    run: death-by-accidents-unnatural-cause-orifice---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule54
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-streetcar---secondary/output
  death-by-accidents-unnatural-cause-submn---secondary:
    run: death-by-accidents-unnatural-cause-submn---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule55
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-orifice---secondary/output
  death-by-accidents-unnatural-cause-agricult---secondary:
    run: death-by-accidents-unnatural-cause-agricult---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule56
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-submn---secondary/output
  death-by-accidents-unnatural-cause-millipede---secondary:
    run: death-by-accidents-unnatural-cause-millipede---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule57
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-agricult---secondary/output
  death-by-accidents-unnatural-cause-stampede---secondary:
    run: death-by-accidents-unnatural-cause-stampede---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule58
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-millipede---secondary/output
  death-by-accidents-unnatural-cause-scaffolding---secondary:
    run: death-by-accidents-unnatural-cause-scaffolding---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule59
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-stampede---secondary/output
  death-by-accidents-unnatural-cause-wheelchair---secondary:
    run: death-by-accidents-unnatural-cause-wheelchair---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule60
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-scaffolding---secondary/output
  death-by-accidents-unnatural-cause-eruption---secondary:
    run: death-by-accidents-unnatural-cause-eruption---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule61
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-wheelchair---secondary/output
  death-by-accidents-unnatural-cause-pushing---secondary:
    run: death-by-accidents-unnatural-cause-pushing---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule62
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-eruption---secondary/output
  death-by-accidents-unnatural-cause-service---secondary:
    run: death-by-accidents-unnatural-cause-service---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule63
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-pushing---secondary/output
  death-by-accidents-unnatural-cause-privation---secondary:
    run: death-by-accidents-unnatural-cause-privation---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule64
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-service---secondary/output
  death-by-accidents-unnatural-cause-steam---secondary:
    run: death-by-accidents-unnatural-cause-steam---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule65
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-privation---secondary/output
  death-by-accidents-unnatural-cause-arthropod---secondary:
    run: death-by-accidents-unnatural-cause-arthropod---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule66
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-steam---secondary/output
  death-by-accidents-unnatural-cause-reptile---secondary:
    run: death-by-accidents-unnatural-cause-reptile---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule67
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-arthropod---secondary/output
  death-by-accidents-unnatural-cause-entering---secondary:
    run: death-by-accidents-unnatural-cause-entering---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule68
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-reptile---secondary/output
  death-by-accidents-unnatural-cause-stumbling---secondary:
    run: death-by-accidents-unnatural-cause-stumbling---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule69
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-entering---secondary/output
  death-by-accidents-unnatural-cause-psytrop---secondary:
    run: death-by-accidents-unnatural-cause-psytrop---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule70
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-stumbling---secondary/output
  death-by-accidents-unnatural-cause-firearm---secondary:
    run: death-by-accidents-unnatural-cause-firearm---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule71
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-psytrop---secondary/output
  death-by-accidents-unnatural-cause-glass---secondary:
    run: death-by-accidents-unnatural-cause-glass---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule72
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-firearm---secondary/output
  death-by-accidents-unnatural-cause-allterr---secondary:
    run: death-by-accidents-unnatural-cause-allterr---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule73
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-glass---secondary/output
  death-by-accidents-unnatural-cause-projected---secondary:
    run: death-by-accidents-unnatural-cause-projected---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule74
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-allterr---secondary/output
  death-by-accidents-unnatural-cause-presurized---secondary:
    run: death-by-accidents-unnatural-cause-presurized---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule75
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-projected---secondary/output
  death-by-accidents-unnatural-cause-tract---secondary:
    run: death-by-accidents-unnatural-cause-tract---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule76
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-presurized---secondary/output
  death-by-accidents-unnatural-cause-transp---secondary:
    run: death-by-accidents-unnatural-cause-transp---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule77
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-tract---secondary/output
  death-by-accidents-unnatural-cause-animalrider---secondary:
    run: death-by-accidents-unnatural-cause-animalrider---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule78
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-transp---secondary/output
  death-by-accidents-unnatural-cause-unpowered---secondary:
    run: death-by-accidents-unnatural-cause-unpowered---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule79
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-animalrider---secondary/output
  death-by-accidents-unnatural-cause-alligator---secondary:
    run: death-by-accidents-unnatural-cause-alligator---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule80
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-unpowered---secondary/output
  larger-death-by-accidents-unnatural-cause---secondary:
    run: larger-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule81
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-alligator---secondary/output
  death-by-accidents-unnatural-cause-fluid---secondary:
    run: death-by-accidents-unnatural-cause-fluid---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule82
      potentialCases:
        id: potentialCases
        source: larger-death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-vibration---secondary:
    run: death-by-accidents-unnatural-cause-vibration---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule83
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-fluid---secondary/output
  death-by-accidents-unnatural-cause-bitten---secondary:
    run: death-by-accidents-unnatural-cause-bitten---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule84
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-vibration---secondary/output
  death-by-accidents-unnatural-cause-movement---secondary:
    run: death-by-accidents-unnatural-cause-movement---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule85
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-bitten---secondary/output
  content-death-by-accidents-unnatural-cause---secondary:
    run: content-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule86
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-movement---secondary/output
  death-by-accidents-unnatural-cause-liting---secondary:
    run: death-by-accidents-unnatural-cause-liting---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule87
      potentialCases:
        id: potentialCases
        source: content-death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-another---secondary:
    run: death-by-accidents-unnatural-cause-another---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule88
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-liting---secondary/output
  death-by-accidents-unnatural-cause-playground---secondary:
    run: death-by-accidents-unnatural-cause-playground---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule89
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-another---secondary/output
  death-by-accidents-unnatural-cause-craft---secondary:
    run: death-by-accidents-unnatural-cause-craft---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule90
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-playground---secondary/output
  death-by-accidents-unnatural-cause-nonmotor---secondary:
    run: death-by-accidents-unnatural-cause-nonmotor---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule91
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-craft---secondary/output
  death-by-accidents-unnatural-cause-lizard---secondary:
    run: death-by-accidents-unnatural-cause-lizard---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule92
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-nonmotor---secondary/output
  death-by-accidents-unnatural-cause-cliff---secondary:
    run: death-by-accidents-unnatural-cause-cliff---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule93
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-lizard---secondary/output
  death-by-accidents-unnatural-cause-pedesn---secondary:
    run: death-by-accidents-unnatural-cause-pedesn---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule94
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-cliff---secondary/output
  mammal-death-by-accidents-unnatural-cause---secondary:
    run: mammal-death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule95
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-pedesn---secondary/output
  death-by-accidents-unnatural-cause-earth---secondary:
    run: death-by-accidents-unnatural-cause-earth---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule96
      potentialCases:
        id: potentialCases
        source: mammal-death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-merchant---secondary:
    run: death-by-accidents-unnatural-cause-merchant---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule97
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-earth---secondary/output
  death-by-accidents-unnatural-cause-prolonged---secondary:
    run: death-by-accidents-unnatural-cause-prolonged---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule98
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-merchant---secondary/output
  death-by-accidents-unnatural-cause---secondary:
    run: death-by-accidents-unnatural-cause---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule99
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-prolonged---secondary/output
  death-by-accidents-unnatural-cause-institution---secondary:
    run: death-by-accidents-unnatural-cause-institution---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule100
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause---secondary/output
  death-by-accidents-unnatural-cause-stock---secondary:
    run: death-by-accidents-unnatural-cause-stock---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule101
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-institution---secondary/output
  death-by-accidents-unnatural-cause-occurrence---secondary:
    run: death-by-accidents-unnatural-cause-occurrence---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule102
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-stock---secondary/output
  death-by-accidents-unnatural-cause-traff---secondary:
    run: death-by-accidents-unnatural-cause-traff---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule103
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-occurrence---secondary/output
  output-cases:
    run: output-cases.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule104
      potentialCases:
        id: potentialCases
        source: death-by-accidents-unnatural-cause-traff---secondary/output
class: Workflow
inputs:
  inputModule1:
    id: inputModule1
    doc: Js implementation unit
    type: File
  inputModule2:
    id: inputModule2
    doc: Python implementation unit
    type: File
  inputModule3:
    id: inputModule3
    doc: Python implementation unit
    type: File
  inputModule4:
    id: inputModule4
    doc: Python implementation unit
    type: File
  inputModule5:
    id: inputModule5
    doc: Python implementation unit
    type: File
  inputModule6:
    id: inputModule6
    doc: Python implementation unit
    type: File
  inputModule7:
    id: inputModule7
    doc: Python implementation unit
    type: File
  inputModule8:
    id: inputModule8
    doc: Python implementation unit
    type: File
  inputModule9:
    id: inputModule9
    doc: Python implementation unit
    type: File
  inputModule10:
    id: inputModule10
    doc: Python implementation unit
    type: File
  inputModule11:
    id: inputModule11
    doc: Python implementation unit
    type: File
  inputModule12:
    id: inputModule12
    doc: Python implementation unit
    type: File
  inputModule13:
    id: inputModule13
    doc: Python implementation unit
    type: File
  inputModule14:
    id: inputModule14
    doc: Python implementation unit
    type: File
  inputModule15:
    id: inputModule15
    doc: Python implementation unit
    type: File
  inputModule16:
    id: inputModule16
    doc: Python implementation unit
    type: File
  inputModule17:
    id: inputModule17
    doc: Python implementation unit
    type: File
  inputModule18:
    id: inputModule18
    doc: Python implementation unit
    type: File
  inputModule19:
    id: inputModule19
    doc: Python implementation unit
    type: File
  inputModule20:
    id: inputModule20
    doc: Python implementation unit
    type: File
  inputModule21:
    id: inputModule21
    doc: Python implementation unit
    type: File
  inputModule22:
    id: inputModule22
    doc: Python implementation unit
    type: File
  inputModule23:
    id: inputModule23
    doc: Python implementation unit
    type: File
  inputModule24:
    id: inputModule24
    doc: Python implementation unit
    type: File
  inputModule25:
    id: inputModule25
    doc: Python implementation unit
    type: File
  inputModule26:
    id: inputModule26
    doc: Python implementation unit
    type: File
  inputModule27:
    id: inputModule27
    doc: Python implementation unit
    type: File
  inputModule28:
    id: inputModule28
    doc: Python implementation unit
    type: File
  inputModule29:
    id: inputModule29
    doc: Python implementation unit
    type: File
  inputModule30:
    id: inputModule30
    doc: Python implementation unit
    type: File
  inputModule31:
    id: inputModule31
    doc: Python implementation unit
    type: File
  inputModule32:
    id: inputModule32
    doc: Python implementation unit
    type: File
  inputModule33:
    id: inputModule33
    doc: Python implementation unit
    type: File
  inputModule34:
    id: inputModule34
    doc: Python implementation unit
    type: File
  inputModule35:
    id: inputModule35
    doc: Python implementation unit
    type: File
  inputModule36:
    id: inputModule36
    doc: Python implementation unit
    type: File
  inputModule37:
    id: inputModule37
    doc: Python implementation unit
    type: File
  inputModule38:
    id: inputModule38
    doc: Python implementation unit
    type: File
  inputModule39:
    id: inputModule39
    doc: Python implementation unit
    type: File
  inputModule40:
    id: inputModule40
    doc: Python implementation unit
    type: File
  inputModule41:
    id: inputModule41
    doc: Python implementation unit
    type: File
  inputModule42:
    id: inputModule42
    doc: Python implementation unit
    type: File
  inputModule43:
    id: inputModule43
    doc: Python implementation unit
    type: File
  inputModule44:
    id: inputModule44
    doc: Python implementation unit
    type: File
  inputModule45:
    id: inputModule45
    doc: Python implementation unit
    type: File
  inputModule46:
    id: inputModule46
    doc: Python implementation unit
    type: File
  inputModule47:
    id: inputModule47
    doc: Python implementation unit
    type: File
  inputModule48:
    id: inputModule48
    doc: Python implementation unit
    type: File
  inputModule49:
    id: inputModule49
    doc: Python implementation unit
    type: File
  inputModule50:
    id: inputModule50
    doc: Python implementation unit
    type: File
  inputModule51:
    id: inputModule51
    doc: Python implementation unit
    type: File
  inputModule52:
    id: inputModule52
    doc: Python implementation unit
    type: File
  inputModule53:
    id: inputModule53
    doc: Python implementation unit
    type: File
  inputModule54:
    id: inputModule54
    doc: Python implementation unit
    type: File
  inputModule55:
    id: inputModule55
    doc: Python implementation unit
    type: File
  inputModule56:
    id: inputModule56
    doc: Python implementation unit
    type: File
  inputModule57:
    id: inputModule57
    doc: Python implementation unit
    type: File
  inputModule58:
    id: inputModule58
    doc: Python implementation unit
    type: File
  inputModule59:
    id: inputModule59
    doc: Python implementation unit
    type: File
  inputModule60:
    id: inputModule60
    doc: Python implementation unit
    type: File
  inputModule61:
    id: inputModule61
    doc: Python implementation unit
    type: File
  inputModule62:
    id: inputModule62
    doc: Python implementation unit
    type: File
  inputModule63:
    id: inputModule63
    doc: Python implementation unit
    type: File
  inputModule64:
    id: inputModule64
    doc: Python implementation unit
    type: File
  inputModule65:
    id: inputModule65
    doc: Python implementation unit
    type: File
  inputModule66:
    id: inputModule66
    doc: Python implementation unit
    type: File
  inputModule67:
    id: inputModule67
    doc: Python implementation unit
    type: File
  inputModule68:
    id: inputModule68
    doc: Python implementation unit
    type: File
  inputModule69:
    id: inputModule69
    doc: Python implementation unit
    type: File
  inputModule70:
    id: inputModule70
    doc: Python implementation unit
    type: File
  inputModule71:
    id: inputModule71
    doc: Python implementation unit
    type: File
  inputModule72:
    id: inputModule72
    doc: Python implementation unit
    type: File
  inputModule73:
    id: inputModule73
    doc: Python implementation unit
    type: File
  inputModule74:
    id: inputModule74
    doc: Python implementation unit
    type: File
  inputModule75:
    id: inputModule75
    doc: Python implementation unit
    type: File
  inputModule76:
    id: inputModule76
    doc: Python implementation unit
    type: File
  inputModule77:
    id: inputModule77
    doc: Python implementation unit
    type: File
  inputModule78:
    id: inputModule78
    doc: Python implementation unit
    type: File
  inputModule79:
    id: inputModule79
    doc: Python implementation unit
    type: File
  inputModule80:
    id: inputModule80
    doc: Python implementation unit
    type: File
  inputModule81:
    id: inputModule81
    doc: Python implementation unit
    type: File
  inputModule82:
    id: inputModule82
    doc: Python implementation unit
    type: File
  inputModule83:
    id: inputModule83
    doc: Python implementation unit
    type: File
  inputModule84:
    id: inputModule84
    doc: Python implementation unit
    type: File
  inputModule85:
    id: inputModule85
    doc: Python implementation unit
    type: File
  inputModule86:
    id: inputModule86
    doc: Python implementation unit
    type: File
  inputModule87:
    id: inputModule87
    doc: Python implementation unit
    type: File
  inputModule88:
    id: inputModule88
    doc: Python implementation unit
    type: File
  inputModule89:
    id: inputModule89
    doc: Python implementation unit
    type: File
  inputModule90:
    id: inputModule90
    doc: Python implementation unit
    type: File
  inputModule91:
    id: inputModule91
    doc: Python implementation unit
    type: File
  inputModule92:
    id: inputModule92
    doc: Python implementation unit
    type: File
  inputModule93:
    id: inputModule93
    doc: Python implementation unit
    type: File
  inputModule94:
    id: inputModule94
    doc: Python implementation unit
    type: File
  inputModule95:
    id: inputModule95
    doc: Python implementation unit
    type: File
  inputModule96:
    id: inputModule96
    doc: Python implementation unit
    type: File
  inputModule97:
    id: inputModule97
    doc: Python implementation unit
    type: File
  inputModule98:
    id: inputModule98
    doc: Python implementation unit
    type: File
  inputModule99:
    id: inputModule99
    doc: Python implementation unit
    type: File
  inputModule100:
    id: inputModule100
    doc: Python implementation unit
    type: File
  inputModule101:
    id: inputModule101
    doc: Python implementation unit
    type: File
  inputModule102:
    id: inputModule102
    doc: Python implementation unit
    type: File
  inputModule103:
    id: inputModule103
    doc: Python implementation unit
    type: File
  inputModule104:
    id: inputModule104
    doc: Python implementation unit
    type: File
outputs:
  cases:
    id: cases
    type: File
    outputSource: output-cases/output
    outputBinding:
      glob: '*.csv'
requirements:
  SubworkflowFeatureRequirement: {}
