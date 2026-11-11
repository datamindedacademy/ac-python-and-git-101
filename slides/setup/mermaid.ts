import { defineMermaidSetup } from '@slidev/types'

// Dataminded palette for every Mermaid diagram: navy main, violet and lavender branches.
export default defineMermaidSetup(() => ({
  theme: 'base',
  themeVariables: {
    fontFamily: 'DM Sans',
    primaryColor: '#e9edff',
    primaryBorderColor: '#543edc',
    primaryTextColor: '#080635',
    lineColor: '#543edc',
    edgeLabelBackground: '#ffffff',
    git0: '#080635',
    git1: '#543edc',
    git2: '#8fdb3d',
    git3: '#9b8cf0',
    git4: '#cacdf9',
    gitBranchLabel0: '#ffffff',
    gitBranchLabel1: '#ffffff',
    gitBranchLabel2: '#080635',
    gitBranchLabel3: '#ffffff',
    gitBranchLabel4: '#080635',
    commitLabelColor: '#080635',
    commitLabelBackground: '#ffffff',
    tagLabelColor: '#080635',
    tagLabelBackground: '#e9edff',
    tagLabelBorder: '#543edc',
  },
}))
